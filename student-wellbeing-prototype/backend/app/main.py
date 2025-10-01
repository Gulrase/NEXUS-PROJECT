from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, chat, risk
from .db import engine
import os
import subprocess
app = FastAPI(title="Student Wellbeing Prototype")

# create tables if not present
try:
    # execute init SQL
    p = os.path.join(os.path.dirname(__file__), "..", "init_db.sql")
    subprocess.call(["bash", "-lc", f"psql {os.getenv('DATABASE_URL')} -f {p}"], shell=False)
except Exception:
    pass

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(risk.router, prefix="/risk")

@app.get("/")
async def root():
    return {"status": "ok", "service": "student-wellbeing-prototype"}
