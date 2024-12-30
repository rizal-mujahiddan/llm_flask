from flask import Flask,render_template

from routing.backend_api.llm_controller import llm_blueprint

app = Flask(__name__,template_folder='views')

app.register_blueprint(llm_blueprint)

@app.get("/")
def hello_world():
    return render_template('index.html')