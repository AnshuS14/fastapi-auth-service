from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@router.get("/user/{id}")
def get_user(id:int):
    return {"user_id": id, "name": f"User{id}"} 

@router.post("/create")
def create_user(name: str):
    return {"message": f"User '{name}' created successfully!"}
