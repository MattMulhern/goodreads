#!/usr/bin/env python3
"""
Example usage of:
- obtaining a user's shelves.
- obtaining the books on that shelf.
"""

from goodreads import client
from datetime import datetime
import argparse
import ics
import sys


def generate_calendar_description(book):
    arr = ["",
           "Title: {0}".format(book.title),
           "Goodreads Link: {0}".format(book.link),
           "",
           "{0}".format(book.description)]
    return "\n".join(arr)


def get_dates_to_read(gc, user):

    shelves = user.shelves()

    tr = shelves[-1]
    books = tr.books
    now = datetime.now()
    unknown_books = []
    upcoming_books = []
    published_books = []
    for title, book in books.items():
        if book.publication_date:
            pubdate = book.publication_date
            if pubdate <= now:
                published_books.append(book)
            elif pubdate > now:
                upcoming_books.append(book)

        elif book.work.publication_date:
            pubdate = book.work.publication_date
            if pubdate <= now:
                published_books.append(book)
            elif pubdate > now:
                upcoming_books.append(book)
        else:
            pubdate = None

    return unknown_books, published_books, upcoming_books


def generate_calendar(books):
    cal = ics.Calendar()
    for book in books:
        pubdate = None
        if book.publication_date:
            pubdate = book.publication_date
        elif book.work.publication_date:
            pubdate = book.work.publication_date

        event = ics.Event(name=book.title,
                          begin=pubdate,
                          description=generate_calendar_description(book))
        event.make_all_day()

        cal.events.append(event)

    return cal


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='goodreads calendar example')
    parser.add_argument('--api-token',
                        help='The api token generated from https://www.goodreads.com/api/keys')
    parser.add_argument('--api-secret',
                        help='The api secret generated from https://www.goodreads.com/api/keys')
    parser.add_argument('--access-token',
                        help='The oath token generated the first time you run this script')
    parser.add_argument('--access-token-secret',
                        help='The oath token secret generated the first time you run this script')
    args = parser.parse_args()

    if not args.access_token or not args.access_token_secret:
        if args.api_token and args.api_secret:
            gc = client.GoodreadsClient(args.api_token, args.api_secret)
            gc.authenticate()
            print("Now rerun script with --api-token --api-secret --access-token and --access-token-secret specified")
            sys.exit(0)
        else:
            print ("Error: must specify api-key and api-token.")
            parser.print_help()
            sys.exit(1)

    gc = client.GoodreadsClient(args.api_token, args.api_secret)
    gc.authenticate(args.access_token, args.access_token_secret)

    user = gc.user()

    unknown_books, published_books, upcoming_books = get_dates_to_read(gc, user)
    cal = generate_calendar(upcoming_books)
    with open('goodreads.ics', 'w') as f:
        f.writelines(cal)
