from pydantic import BaseModel

class Result(BaseModel):
    value: str
class Contact(BaseModel):
    urn : str
class Results(BaseModel):
    result : Result

class MainInput(BaseModel):
    contact: Contact
    results : Results
