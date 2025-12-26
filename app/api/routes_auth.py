from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_access_token

# Initialize the API router
router = APIRouter()

# Pydantic model for input data
class AuthInput(BaseModel):
    username: str
    password: str

# The login endpoint
@router.post('/login')
def login(auth: AuthInput):
    if (auth.username == "admin") and (auth.password == "admin"):
        token = create_access_token(data={"sub": auth.username})
        return {"access_token": token}
    return {"error": "Invalid Credentials"}