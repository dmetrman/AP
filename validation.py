from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    name = fields.String()
    surname = fields.String()
    username = fields.String(validate=Length(min=6))
    password = fields.String(validate=Length(min=6))


class CarSchema(Schema):
    brand = fields.String(required=True)
    model = fields.String(required=True)
    status = fields.String(required=True)


class OrderSchema(Schema):
    user_id = fields.Integer(required=True)
    car_id = fields.Integer(required=True)
    beginningDate = fields.DateTime(required=True)
    amountOfDays = fields.Integer(required=True)
    complete = fields.String(required=True)