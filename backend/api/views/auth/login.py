from fastapi import Depends, APIRouter
from api.database import get_db, Session, User
from api.schemas.user import LoginModel
from api.services.auth import login as loginSVC
from werkzeug.exceptions import Unauthorized
from api.services.jwt import create_token
from api.schemas.user import LoginResponse
from werkzeug.security import check_password_hash

from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
from typing import Annotated
import hashlib


auth_router = APIRouter()

@auth_router.post("/login", tags=["AUTH"], response_model=LoginResponse)
async def login(credentials:LoginModel, db:Session=Depends(get_db)):
    """User authentication"""
    
    token = loginSVC.login(db, credentials)
    
    return LoginResponse(message={
        "username" : credentials.username,
        "token" : token
    })
    
    
    
@auth_router.post("/doc-login", tags=["AUTH"], include_in_schema=False)
async def docs_login(
        credentials: Annotated[OAuth2PasswordRequestForm, Depends()], 
        db:Session=Depends(get_db)
    ):
    """Doc login"""
    
    return loginSVC.loginDoc(db, credentials)