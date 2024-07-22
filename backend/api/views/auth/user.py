from api.schemas.user import UserResponseListModel, UserResponseModel, UpdateUserModel
from api.schemas.response import Response
from api.services.jwt import getPayload
from api.database import get_db
from api.database import User
from api.services.auth import user as userSVC
from fastapi import  Depends
from fastapi import APIRouter
from .login import auth_router

user_router = APIRouter(dependencies=[Depends(getPayload)])


@auth_router.post("/register", response_model=UserResponseModel, tags=["AUTH"])
def create_user(user:User, db=Depends(get_db)):
    """Create new user"""
    
    new_user = userSVC.create_user(user, db)
    return Response(message=new_user)


@user_router.get("/", response_model=UserResponseListModel, tags=["USER"])
def get_all_user(db=Depends(get_db)): #, actualUser:dict=Depends(getPayload)
    """Get all users"""
    
    users = User.getAll(db=db)
    return Response(message=users)


@user_router.get("/{username}", response_model=UserResponseModel, tags=["USER"])
def get_user_Details(username:str, db=Depends(get_db)):
    """Get users details"""
    
    user = User.get(db=db, username=username)
    return UserResponseModel(message=user)
    
    
@user_router.put("/{username}", response_model=UserResponseModel, tags=["USER"])
def update_user(username, user:UpdateUserModel, db=Depends(get_db)):
    """Update User"""
    
    user_exist = userSVC.update_user(username, user, db)
    return UserResponseModel(message=user_exist)


@user_router.delete("/{username}", response_model=Response, tags=["USER"])
def delete_user(username, db=Depends(get_db)):
    """Delete user"""
    
    user_exist = User.get(username=username, db=db)
    user_exist.deleteWithCommit(db=db)
    
    return Response(message=f"User {username} deleted !")
    

    
    
    