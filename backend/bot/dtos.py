from pydantic import BaseModel

# dtos.py

# API request aur response define karti hai.

class ChatRequest(BaseModel):
  message:str

class ChatResponse(BaseModel):
  response:str
