from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import jwt ,JWTError

from app.core.config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

#hashing and verifying password
pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)

# def hash_password(password:str) -> str:
#     return pwd_context.hash(password)

def hash_password(password: str) -> str:
    print("PASSWORD TYPE:", type(password))
    print("PASSWORD VALUE:", password)
    print("PASSWORD LENGTH:", len(str(password)))

    return pwd_context.hash(password)

def verify_password(
        plain_password:str,
        hashed_password:str
)->bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

#token generation and verification
def create_access_token(data:dict)->str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt


#token decoder



def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        return user_id

    except JWTError:
        return None