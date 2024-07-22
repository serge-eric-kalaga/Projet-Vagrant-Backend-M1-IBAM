from pydantic import BaseModel, Field
from typing import Optional


class LoginModel(BaseModel):
    username: str
    password: str

class LoginResponseModel(BaseModel):
    username: str
    token: str

class LoginResponse(BaseModel):
    status:int = 1 
    message:LoginResponseModel

class UserModel(BaseModel):
    username:str = Field(..., include=True)
    password:Optional[str]
    
class UpdateUserModel(BaseModel):
    username:Optional[str] = None
    password:Optional[str] = None

class UserResponseModel(BaseModel):
    status:int = 1 
    message:UserModel
    
class UserResponseListModel(BaseModel):
    status:int = 1
    message:list[UserModel]