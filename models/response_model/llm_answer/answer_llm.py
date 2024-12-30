from pydantic import BaseModel

class AnswerLlm(BaseModel):
    answer: str
    status: int