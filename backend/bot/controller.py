from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage
from bot.dtos import ChatRequest
from utils.settings import settings
from sqlalchemy.orm import Session
from bot.models import ChatHistory

llm = ChatGroq(model="openai/gpt-oss-120b",
                api_key = settings.GROQ_API_KEY
                 )

def get_bot_response(request:ChatRequest,db:Session):
  
  user_message = request.message

  system_prompt = """
  You are Nexora Bot.
  Your owner is Aniket Underiya.

  Rules:
  - Give short answers.
  - Maximum 3-4 lines.
  - Use Simple Easy English language.
  - Be helpful and professional.

  """

  result = llm.invoke([

    SystemMessage(content=system_prompt),
    HumanMessage(content=user_message)
  ])

  bot_response = result.content
  
  chat = ChatHistory(
                      user_message = user_message,
                      bot_response = bot_response
                    )
  
  db.add(chat)
  db.commit()
  db.refresh(chat)


  return {
    "response": bot_response
  }




  