class WikiWhoAPI:
    def __init__(self, id):
        self.id = id

    def all_content(self):
        return {'page_id': self.id}