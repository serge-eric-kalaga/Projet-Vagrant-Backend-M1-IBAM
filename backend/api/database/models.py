from pydantic import validator
from typing import Optional
from api.database import BaseTemplate
from sqlalchemy import func, Integer, Boolean, DateTime, String, JSON, ForeignKey, Text, ARRAY, Table, Column, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, MappedAsDataclass, DeclarativeBase, relationship, WriteOnlyMapped
from datetime import datetime

class Base(MappedAsDataclass, DeclarativeBase):
    date_creation:Mapped[datetime] = mapped_column(server_default=func.now(), init=False)
    date_modification:Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True, init=False)

class User(Base, BaseTemplate): 
    __tablename__ = "user"
 
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True, init=False)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, unique=True, init=True)
    password: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, init=True)
    
     
    @validator("username")
    def validate_username(cls, username):
        if len(username) < 3 :
            raise ValueError("Le username doit etre superieur a 3 caracteres !")
        return username
    
    @validator("password")
    def validate_password(cls, password):
        if len(password) < 8 :
            raise ValueError("Le password doit etre superieur a 8 caracteres !")
        return password
    


class Task(Base, BaseTemplate):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, init=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, init=True)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, default=None, init=True)
    is_completed: Mapped[Optional[bool]] = mapped_column(Boolean, default=False, nullable=False, init=True)
    