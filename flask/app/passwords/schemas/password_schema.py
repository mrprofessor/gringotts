from app.common.schemas import BaseSchema, fields


class PasswordSchema(BaseSchema):
    uuid = fields.Str(required=False)
    name = fields.Str(required=True)
    login = fields.Str(required=True)
    password = fields.Str(required=True)
