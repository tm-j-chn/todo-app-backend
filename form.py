from marshmallow import Schema, fields

class TodoSchema(Schema):
    context = fields.String(required = True, data_key = "text")