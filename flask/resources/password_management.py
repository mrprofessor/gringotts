import json

class PasswordManagement:
    """ Indie file management class """
    def __init__(self, filename):
        self.filename = filename
        self.passwords = self.read_file()

    def list(self):
        """ Return all records """
        return self.passwords

    def get(self, password_id):
        """ Return a particular record """
        return self.passwords.get(password_id)

    def post(self, pw_key, pw_data):
        """ Append/Update a new record """

        self.passwords[pw_key] = pw_data
        self.rewrite()

    def delete(self, password_id):
        """ delete a particular record """

        if self.passwords.get(password_id):
            del self.passwords[password_id]

        self.rewrite()

    def rewrite(self):
        """ Rewrite the json file """

        buff = open(self.filename, "w")
        with open(self.filename, 'w', encoding='utf-8') as buff:
            json.dump(self.passwords, buff, ensure_ascii=False, indent=4)
        buff.close()

    # TODO
    # 1. Unencrypt file?
    def read_file(self):
        """ Read the password file """

        # Handle file exception
        try:
            buff = open(self.filename, 'rb')
        except (OSError, IOError) as err:
            print("Could not open/read file:", self.filename)
            return err

        # Handler json exception
        try:
            data = json.load(buff)
            buff.close()
        except Exception as err:
            return err

        return data
