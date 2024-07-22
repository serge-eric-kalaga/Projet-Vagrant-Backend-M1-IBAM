from datetime import datetime, timedelta
from api.configs.config import Setting
from jose import jwt, JWTError
from werkzeug.exceptions import Unauthorized, Forbidden
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from api.configs.logging import logResponse
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/doc-login")

def create_token(data:dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Setting.JWT_SECRET, algorithm=Setting.ALGORITHM)
    return encoded_jwt

def decode_token(token:str):
    try:
        payload = jwt.decode(token, Setting.JWT_SECRET, algorithms=[Setting.ALGORITHM])
        logResponse({"payload":payload})
        return payload
    except JWTError:
        return None
    
    
def getPayload(token:str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if payload == None:
        raise Forbidden("Token Invalide")
    return payload

    
def isAdmin(token: oauth2_scheme = Depends(getPayload)):
    if token["role"] == "admin" :
        return token
    raise Unauthorized("Privileges insuffisants")