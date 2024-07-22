from api.schemas.user import UserResponseListModel, UserResponseModel, UpdateUserModel
from werkzeug.security import generate_password_hash
from api.schemas.response import Response
from api.services.jwt import getPayload
from api.database import engine, get_db
from api.database.models import User
from sqlalchemy.orm import Session 
from fastapi import  Depends

def create_user(user:User, db:Session) -> User:
    new_user = User(
        username=user.username,
        password=generate_password_hash(user.password)
    )
    new_user.saveWithCommit(db=db)
    return new_user

def update_user(username:str, user:UpdateUserModel, db:Session) -> User:
    user_exist = User.get(username=username, db=db)
    
    for key, value in user :
        if value is not None :
            setattr(user_exist, key, value)
    user_exist.saveWithCommit(db=db)
    return user_exist