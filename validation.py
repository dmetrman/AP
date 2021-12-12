from marshmallow import Schema, fields
from marshmallow.validate import Length


class UserSchema(Schema):
    name = fields.String()
    surname = fields.String()
    username = fields.String(validate=Length(min=6))
    password = fields.String(validate=Length(min=6))
    role = fields.String()


class CarSchema(Schema):
    brand = fields.String()
    model = fields.String()
    status = fields.String()


class OrderSchema(Schema):
    user_id = fields.Integer()
    car_id = fields.Integer()
    beginningDate = fields.DateTime()
    amountOfDays = fields.Integer()
    complete = fields.String()
