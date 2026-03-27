from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    age: int

user_db = {} 
#creating python dictionary to store user data in memory, fake database for demonstration purposes, it will be lost when the application restarts.

@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


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


@router.post("/create")
def create_user(user: User):
    if user.id in user_db:
        raise HTTPException(status_code=400, detail="User already exists")

    user_db[user.id] = user.dict()

    return {
        "message": "New user created successfully!",
        "user": user
    }
