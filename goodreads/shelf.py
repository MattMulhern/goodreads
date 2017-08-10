from . import book


class GoodreadsShelf:
    def __init__(self, client, shelf_dict):
        self._shelf_dict = shelf_dict
        self._client = client

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

    @property
    def books(self):
        return self.get_books(full=True)

    @property
    def shallow_books(self):
        return self.get_books(full=False)

    def get_books(self, full=True, max_results=200):
        books = {}
        user = self._client.user()
        req = self._client.request("/review/list/%s.xml" % user.gid, {'shelf': self, 'per_page': max_results})

        for i, req_book in enumerate(req['books']['book'], start=1):
            if full:
                print("fetching {0} of {1}: {2}".format(i, len(req['books']['book']), req_book['title']))
                books[req_book['title']] = self._client.book(book_id=req_book['id']['#text'])
            else:
                books[req_book['title']] = book.GoodreadsBook(client=self._client, book_dict=req_book)
        return books
