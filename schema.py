from pydantic import BaseModel, EmailStr 
from enum import Enum
 
 
class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
 
    class Config:
        from_attributes = True
        
        
class Roles(Enum):
    user = "user"
    admin = "admin"