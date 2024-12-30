import json
from models.request_model.llm_question.question_llm import QuestionLlm
from flask import (
    Blueprint,
    request as req_flask,
    redirect
)
llm_blueprint = Blueprint('llm',__name__)

@llm_blueprint.get('/api/v1/rizal')
def rizalku():
    data = {"name": "Alice", "age": 30, "city": "New York"}
    json_data = json.dumps(json_data)
    return redirect