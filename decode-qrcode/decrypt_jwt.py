import jwt
from data import key

def decrypt(token):
    dec = jwt.decode(token, key, verify = True, algorithms=['RS256'])
    return dec