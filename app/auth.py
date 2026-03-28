from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Create an instance of the OAuth2PasswordBearer to handle token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create an instance of the password context to handle password hashing and verification
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

#Hash the password
def hash_password(password: str):
    # truncate to 72 bytes (bcrypt limit)
    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        raise ValueError("Password too long for bcrypt")

    return pwd_context.hash(password)

#Verify the password
def verify_passwor(plain, hashed):
    return pwd_context.verify(plain, hashed)

#Create access token / JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

#Authentication function to verify the user credentials and return a JWT token if valid
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
