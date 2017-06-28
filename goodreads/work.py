"""Goodreads work class"""


class GoodreadsWork:
    def __init__(self, work_dict, client):
        self._work_dict = work_dict
        self._client = client

    def __repr__(self):
        return self.title

    @property
    def gid(self):
        """Goodreads id of the book"""
        return self._work_dict['id']

    @property
    def title(self):
        """Title of the book"""
        return self._work_dict['original_title']

    @property
    def publication_month(self):
        """Original publication month"""
        try:
            val = self._work_dict['original_publication_month']['#text']
        except KeyError:
            return None
        return int(val)

    @property
    def publication_year(self):
        """Original publication year"""
        try:
            val = self._work_dict['original_publication_year']['#text']
        except KeyError:
            return None
        return int(val)

    @property
    def publication_day(self):
        """Original publication day"""
        try:
            val = self._work_dict['original_publication_day']['#text']
        except KeyError:
            return None
        return int(val)
