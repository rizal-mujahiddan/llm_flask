from pydantic import BaseModel

class QuestionLlm(BaseModel):
    question: str