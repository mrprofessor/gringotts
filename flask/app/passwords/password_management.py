import json
from app.common.exceptions import SystemException
from cryptography.fernet import Fernet


class PasswordManagement:
    """ Indie file management class """
    def __init__(self, filename, key):
        """
            filename: relative location of the file
            key: relative location of the key file
        """
        self.key = key
        self.filename = filename
        self.passwords = self.read_file()

    def list(self):
        """ Return all records """
        pw_dict = self.passwords

        pw_list = [{**pw_dict[key], "uuid": key} for key in pw_dict]
        return pw_list

    def get(self, password_id):
        """ Return a particular record """
        pw_record = self.passwords.get(password_id)
        if pw_record:
            pw_record = {**pw_record, "uuid": password_id}
        return pw_record

    def create(self, pw_key, pw_data):
        """ Append/Update a new record """
        self.passwords[pw_key] = pw_data
        self.rewrite()

    def delete(self, password_id):
        """ delete a particular record """
        if self.passwords.get(password_id):
            del self.passwords[password_id]

        self.rewrite()

    def rewrite(self):
        """ Rewrite the password file """
        json_data = json.dumps(self.passwords)
        encrypted_data = self.encrypt_text(str(json_data))
        try:
            buff = open(self.filename, 'w')
            buff.write(encrypted_data)
            buff.close()
        except (OSError, IOError) as err:
            print("Could not open/read file:", self.filename)
            return err

    def read_file(self):
        """ Read the password file """
        try:
            buff = open(self.filename, 'r')
            raw_data = buff.read()
            decrypted_data = self.decrypt_text(raw_data)
            data = json.loads(decrypted_data)
            buff.close()
        except (OSError, IOError) as err:
            print("Could not open/read file:", self.filename)
            return err
        except Exception:
            raise SystemException

        return data

    def encrypt_text(self, input_text):
        """ Encrypt text """
        fercryptor = Fernet(self.key)
        return fercryptor.encrypt(input_text.encode()).decode()

    def decrypt_text(self, input_text):
        """ Decrypt text """
        fercryptor = Fernet(self.key)
        return fercryptor.decrypt(input_text.encode()).decode()

    def encrypt_file(self):
        """ Encrypt the contents of the file """
        fercryptor = Fernet(self.key)

        # Handle file exception
        try:
            buff = open(self.filename, 'r+')
        except (OSError, IOError) as err:
            print("Could not open/read file:", self.filename)
            return err

        try:
            file_data = buff.read().encode()
            encrypted_data = fercryptor.encrypt(file_data)
            buff.seek(0) # move to the start
            buff.write(encrypted_data.decode())
            buff.truncate()
            buff.close()
        except Exception as err:
            return err

    def seed_file(self):
        """ Create and encrypt a new file"""
        data = '{}'
        encrypted_data = self.encrypt_text(data)
        with open('passwords.json', 'w') as buff:
            buff.write(encrypted_data)

    def decrypt_file(self):
        """ Decrypt the contents of the file """
        fercryptor = Fernet(self.key)

        # Handle file exception
        try:
            buff = open(self.filename, 'r+')
            file_data = buff.read().encode()
            buff.seek(0) # move to the start
            decrypted_data = fercryptor.decrypt(file_data)
            buff.write(decrypted_data.decode())
            buff.truncate()
            buff.close()
        except (OSError, IOError) as err:
            print("Could not open/read file:", self.filename)
            return err
        except Exception as err:
            return err
