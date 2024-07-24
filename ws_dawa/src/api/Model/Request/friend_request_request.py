from marshmallow import Schema, fields

class FriendRequestRequest(Schema):
    solicitante_id = fields.Integer(required=True)
    solicitado_id = fields.Integer(required=True)
    estado = fields.String(required=True)
