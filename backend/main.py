from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.db import Base , engine

from bot.routers import router

Base.metadata.create_all(engine)

app = FastAPI(title="This is my Chatbot Application")
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(router)