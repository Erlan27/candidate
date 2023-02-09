from flask import Flask
from classes.candidate import CandidateGetter

app = Flask(__name__)

candidate = CandidateGetter("candidates.json")


@app.route("/")
def page_index():
    return "<pre>" + "\n"+candidate.get_all() + "</pre>"


@app.route("/candidate/")
def info():
    return "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/" \
           "1200px-Python-logo-notext.svg.png' width='100' height='100'>" + "<pre>"+candidate.get_name("Erlan")\
        + "\n" + candidate.get_id("2") + "\n" + candidate.get_skill("python")


app.run()
