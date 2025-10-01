from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Signup(BaseModel):
    email: str
    password: str
    consent: bool = False

@router.post("/signup")
async def signup(payload: Signup):
    # Minimal demo: in real system, hash password and store user
    return {"message": "signup successful (demo)", "email": payload.email}

@router.post("/login")
async def login(email: str, password: str):
    # Always accept for demo
    return {"access_token": "demo-token", "token_type": "bearer"}
