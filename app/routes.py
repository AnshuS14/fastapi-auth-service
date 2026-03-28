from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from jose import jwt

from app.models import User_create, User_In_DB
from app.auth import hash_password, verify_passwor, create_access_token, get_current_user

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    age: int

#creating python dictionary to store user data in memory, fake database for demonstration purposes, it will be lost when the application restarts.
user_db = {} 


#API endpoint to return a welcome message when the root URL is accessed
@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

#API endpoint to retrieve user information based on the provided user ID, 
#it checks if the user exists in the user_db dictionary and returns the user details if found, 
#otherwise it raises a 404 HTTP exception.
@router.get("/user/{id}")
def get_user(id:int):

    user = user_db.get(id)

    if id not in user_db:
        raise HTTPException(status_code=404, detail="User not found")

    print(user_db)
    return {
        "user_id": user["id"],
        "name": user["name"]
    } 

#API endpoint to create a new user, it checks if the user ID already exists in the user_db dictionary and raises a 400 HTTP exception if it does, 
#otherwise it adds the new user to the dictionary and returns a success message along with the user details.
@router.post("/create")
def create_user(user: User):
    if user.id in user_db:
        raise HTTPException(status_code=400, detail="User already exists")

    user_db[user.id] = user.dict()

    return {
        "message": "New user created successfully!",
        "user": user
    }

#API endpoint to register a new user, it checks if the username already exists in the user_db dictionary 
#and raises a 400 HTTP exception if it does, otherwise it hashes the user's password, creates a new user entry in the dictionary, and returns a success
@router.post("/register_user")
def register_user(user: User_create):
    if user.username in user_db:
        raise HTTPException(status_code=400, detail="User already exists")

    print("RAW USER OBJECT:", user)
    print("USERNAME:", user.username)
    print("PASSWORD:", user.password)
    print("PASSWORD LENGTH:", len(user.password))
    print("PASSWORD BYTES:", len(user.password.encode("utf-8")))
    
    hashed_password = hash_password(user.password)

    user_in_db = User_In_DB(username=user.username, hashed_password=hashed_password)

    user_db[user.username] = user_in_db.dict()

    return {
        "message": "New user registered successfully!",
        "user": user.username
    }

#API endpoint to handle user login, it checks if the provided username exists in the user_db dictionary 
#and if the provided password matches the stored hashed password,
@router.post("/login")
def login(user: User_create):
    user_in_db = user_db.get(user.username)

    if not user_in_db:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_passwor(user.password, user_in_db["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

#API endpoint to demonstrate a protected route that requires authentication, 
#it uses the get_current_user function to verify the JWT token and retrieve the current user's information,
@router.get("/protected")
def protected_route(user: str = Depends(get_current_user)):
    return {"message": f"Hello {user}, you are authorized"}
    