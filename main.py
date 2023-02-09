from flask import Flask
from classes.candidate import CandidateGetter

app = Flask(__name__)

candidate_getter = CandidateGetter("candidates.json")


@app.route('/')
def page_index():
    return "Привет я главная страничка"
