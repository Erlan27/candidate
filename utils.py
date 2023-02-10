import json


def load_file():
    with open("candidates.json") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates
