class CandidateGetter:
    def __init__(self, path):
        self.path = path

    def get_name(self, name):
        return name

    def get_id(self, id_):
        return id_

    def get_skill(self, skill):
        return skill

    def get_all(self):
        data = self.path
        return data
