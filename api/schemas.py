#from marshmallow import INCLUDE
from api.app import ma

class TokenResponseSchema(ma.Schema):
    access_token = ma.Str(required=True)