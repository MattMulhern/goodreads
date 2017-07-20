from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.work import GoodreadsWork

from datetime import datetime


class TestBook():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.book = client.book('228665')
        cls.work = cls.book.work

    def test_get_work(self):
        assert isinstance(self.work, GoodreadsWork)
        assert self.work.gid == '2008238'
        assert repr(self.work) == 'The Eye of the World'

    def test_publication_date(self):
        assert self.work.publication_date == datetime(1990, 1, 15, 0, 0)
