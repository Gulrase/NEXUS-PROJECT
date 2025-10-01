from fastapi import APIRouter, Body
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os

router = APIRouter()
embed_model = SentenceTransformer("all-MiniLM-L6-v2")  # small & fast

class ChatIn(BaseModel):
    user_id: str
    message: str

@router.post("/message")
async def message(payload: ChatIn):
    # 1) store message (omitted DB write for brevity)
    # 2) compute embedding
    emb = embed_model.encode(payload.message, convert_to_numpy=True)
    emb_list = emb.tolist()
    # 3) compute simple sentiment (demo): negative if contains "sad","depress"
    negative_words = ["sad","depress","hopeless","anxious","stressed","stress"]
    sentiment = {"valence": -0.5} if any(w in payload.message.lower() for w in negative_words) else {"valence": 0.5}
    # 4) compute reply: try local TGI if available (demo fallback)
    reply = "Thanks for sharing — I'm here to help. Would you like breathing exercises or study tips?"
    return {"reply": reply, "sentiment": sentiment, "embedding_len": len(emb_list)}
