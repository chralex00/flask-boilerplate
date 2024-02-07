from datetime import date
from marshmallow import fields, validate, Schema

class CreateUpdatePerson(Schema):
    first_name = fields.String(required = True, validate = validate.Length(min = 1, max = 128))
    last_name = fields.String(required = True, validate = validate.Length(min = 1, max = 128))
    birthday_year = fields.Integer(required = True, validate = validate.Range(min = date.today().year - 140, max = date.today().year))
    gender = fields.String(required = True, validate = validate.OneOf(["MALE", "FEMALE", "OTHER"]))
    email = fields.Email(required = True, vlaidate = validate.Length(min = 1, max = 256))