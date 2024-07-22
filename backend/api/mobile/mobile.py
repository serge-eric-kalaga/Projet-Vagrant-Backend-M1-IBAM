from api.schemas.response import Response
from api.configs import Setting
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from werkzeug.exceptions import BadRequest
import base64
import binascii

class State: 
    state_code :str =""
    iv: str = ""
    crypted:bool = False 

state = State()

def genKey(code:str):
    return f"{4*code}"

def genPassword(length:int=4):
    assert(length >= 1)
    import random
    return random.randint((10**length), (10**(length+1)-1))

def split(payload:dict) -> tuple[str, str, str]:
        numero:str = payload['contact']['urn'][4:]
        message:str =  payload['results']["result"]["value"]
        crypt_message = message[4:]
        code:str = message[:3]
        return (code, numero, crypt_message)

def crypt(key:str, message:str):
    secret = Setting.SECRET_KEY.encode()
    iv = key.encode()
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    return base64.b64encode(cipher.encrypt(pad(message.encode(), AES.block_size))).decode()

def decrypt(key:str, message:str):
    """
        decrypt work
    """
    secret = Setting.SECRET_KEY.encode()
    try:
        enc = base64.b64decode(message)
    except binascii.Error as exp:
        raise BadRequest(str(exp)+" message Not crypt Correctly")
    #print("enc:", enc)
    iv = key.encode()
    try:
        cipher = AES.new(secret, AES.MODE_CBC, iv)
        result = cipher.decrypt(enc)
        #print('cipher:',result)
        return unpad(result, AES.block_size).decode('utf-8')
    except ValueError as exp:
        raise BadRequest(str(exp))

def response(status:int=1, message:str= "", data:str|None=None) -> Response:
    if state.crypted:
        message = crypt(state.iv, message)
    if data is not None and state.crypted:
        data = crypt(state.iv, data)
    if state.state_code !="":
        message = f"{state.state_code} "+message
        if data is not None:
            data = f"{state.state_code} "+data
    return Response(status=status, message=message, data=data)