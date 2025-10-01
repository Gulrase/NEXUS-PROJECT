from fastapi import APIRouter
import numpy as np
import joblib
from pydantic import BaseModel

router = APIRouter()

class ScoreIn(BaseModel):
    user_id: str
    features: dict

@router.post("/score")
async def score(payload: ScoreIn):
    # For demo: if features contain low attendance or low gpa -> raise risk
    feats = payload.features
    score = 0.1
    if feats.get("attendance_percent", 100) < 75:
        score += 0.4
    if feats.get("gpa", 4.0) < 2.2:
        score += 0.4
    score = min(score, 0.99)
    return {"user_id": payload.user_id, "score": score, "model_version": "demo-v1"}
