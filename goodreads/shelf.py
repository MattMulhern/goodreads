
class GoodreadsShelf:
    def __init__(self, shelf_dict):
        self._shelf_dict = shelf_dict

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._shelf_dict['name']

    @property
    def id(self):
        return int(self._shelf_dict['id']['#text'])

    @property
    def count(self):
        return int(self._shelf_dict['book_count']['#text'])
