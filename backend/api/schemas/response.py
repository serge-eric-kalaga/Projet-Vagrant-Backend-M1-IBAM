from pydantic import BaseModel
from typing import Generic, TypeVar
from pydantic import BaseModel

TypeX = TypeVar('TypeX')
class Response(BaseModel, Generic[TypeX]):
    status:int = 1
    message:TypeX|str


#class Response(BaseModel):
    #status:int
    #message:str
    #data:str|None