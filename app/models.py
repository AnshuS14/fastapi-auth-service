from pydantic import BaseModel, field_validator

class User_create(BaseModel):
    username: str
    password: str

    @field_validator("password")
    def validate_password_length(cls, value):
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password too long (max 72 bytes)")
        return value

class User_In_DB(BaseModel):
    username: str
    hashed_password: str

