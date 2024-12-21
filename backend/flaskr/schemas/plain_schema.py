from marshmallow import Schema, fields, validate

class PlainTaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True, data_key="createdAt")
