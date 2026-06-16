from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from utils.db import get_db
from bot.dtos import ChatRequest
from bot.controller import get_bot_response

router = APIRouter()


@router.post("/chat")
def chat(request:ChatRequest,db:Session=Depends(get_db)):
  return get_bot_response(request,db)



