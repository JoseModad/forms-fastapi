from passlib.context import CryptContext
from jose import jwt
from models import UserModel
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, Request
from models import UserModel


JWT_SECRET="cairocoders$§%§$Ednalan"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=3000

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")


# Save token to oauth2_scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "user/signin")
COOKIE_NAME = "Authorization"


# Create Token
def create_access_token(user):
    try:
        payload = {
			"username" : user.username,
			"email" : user.email,
			"role" : user.role.value if user.role else None,
			"active" : user.is_active,
		}
        return jwt.encode(payload, key = JWT_SECRET, algorithm = ALGORITHM)
    
    except Exception as ex:
        print(str(ex), "aca se imprimio")
        raise ex
    
    
def verify_token(token):
    try:
        payload = jwt.decode(token, key = JWT_SECRET)
        return payload
    except Exception as ex:
        print(str(ex))
        raise ex 
    
       

# Password hash
def get_password_hash(password):
    return pwd_context.hash(password)


# Password verify
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def get_current_user_from_token(token : str = Depends(oauth2_scheme)):
    user = verify_token(token)
    return user


def get_current_user_from_cookie(request : Request) -> UserModel:
    token = request.cookies.get(COOKIE_NAME)
    if token:
        user = verify_token(token)
        return user