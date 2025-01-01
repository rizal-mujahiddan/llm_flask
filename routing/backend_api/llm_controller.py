from transformers import pipeline

import json
from models.request_model.llm_question.question_llm import QuestionLlm
from flask import (
    Blueprint,
    request as req_flask,
    redirect
)
llm_blueprint = Blueprint('llm',__name__)


def inf_llm(stringku):
    generator = pipeline(model="google/flan-t5-small")
    outputs = generator(stringku, num_return_sequences=1)
    return outputs[0]['generated_text']

@llm_blueprint.get('/api/v1/rizal')
def rizalku():
    data = req_flask.values.get('question')
    outputnya = inf_llm(data)
    return outputnya