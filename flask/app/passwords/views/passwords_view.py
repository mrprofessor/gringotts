from flask import request, current_app as app
from app.common.views import BaseView
from app.common.exceptions import NotFoundException
from ..password_management import PasswordManagement
from app.common.representations import output_json
from ..schemas.password_schema import PasswordSchema
import uuid

key = app.config.get('CRYPTO_KEY')
filename = app.config.get('PASSWORD_FILE')
pm = PasswordManagement(filename, key)


class PasswordsView(BaseView):
    representations = {'application/json': output_json}

    def index(self):
        return self.load_input_data(PasswordSchema(many=True), pm.list()), 200

    def get(self, pw_id):
        data = pm.get(pw_id)
        if data:
            return PasswordSchema().dump(data), 200
        else:
            raise NotFoundException()

    def delete(self, pw_id):
        data = pm.get(pw_id)
        if data:
            pm.delete(pw_id)
            return {"message": "Successfully deleted"}, 201
        else:
            raise NotFoundException()

    def post(self):
        pw_input = self.load_input_data(PasswordSchema(), request.json)
        pw_id = str(uuid.uuid4())
        pm.create(pw_id, pw_input)
        return pm.get(pw_id), 201

    def put(self, pw_id):
        pw_input = self.load_input_data(PasswordSchema(), request.json)
        if pm.get(pw_id):
            pm.create(pw_id, pw_input)
            return pm.get(pw_id), 201
        else:
            raise NotFoundException()

