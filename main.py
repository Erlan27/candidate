from flask import Flask
import utils

app = Flask(__name__)

candidates = utils.load_file()


@app.route("/")
def page_index():

    str_candidates = "<pre>"
    for i in candidates.values():
        str_candidates += f"{i['name']} {i['id']} {i['skill']}\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidates/<int:id>")
def info(id):
    img = "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/" \
           "1200px-Python-logo-notext.svg.png' width='100' height='100'>"
    profile = candidates[id]
    str_candidates = f"{profile['name']}\n {profile['id']}\n {profile['skill']}\n"
    return img + str_candidates


app.run()
