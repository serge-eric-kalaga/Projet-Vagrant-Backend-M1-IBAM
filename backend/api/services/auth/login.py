from api.database.models import User
from api.schemas.user import LoginModel
from werkzeug.exceptions import Unauthorized
from api.services.jwt import create_token
from werkzeug.security import check_password_hash

def login(db, credentials:LoginModel) -> str:
    user_exist:User = User.getOrNone(db=db, username=credentials.username) 
    
    # print(user_exist.password)
    
    if user_exist is None or  not check_password_hash(user_exist.password, credentials.password) : 
        raise Unauthorized(description="Username / Mot de passe incorrest !")
    
    token = create_token(data={"username":credentials.username})
    return token

def loginDoc(db, credentials:LoginModel) -> dict[str, str]:
    token = login(db, credentials)
    result = {"access_token": token, "token_type": "bearer"}
    return result