"""Goodreads work class"""
from datetime import datetime


class GoodreadsWork:
    def __init__(self, work_dict, client):
        self._work_dict = work_dict
        self._client = client

    def __repr__(self):
        return self.title

    @property
    def gid(self):
        """Goodreads id of the book"""
        return self._work_dict['id']['#text']

    @property
    def title(self):
        """Title of the book"""
        return self._work_dict['original_title']

    @property
    def publication_month(self):
        """Original publication month"""
        try:
            val = self._work_dict['original_publication_month']['#text']
            ival = int(val)
        except KeyError:  # May not be present
            return None
        except TypeError:  # May be present None
            return None
        return ival

    @property
    def publication_year(self):
        """Original publication year"""
        try:
            val = self._work_dict['original_publication_year']['#text']
            ival = int(val)
        except KeyError:  # May not be present
            return None
        except TypeError:  # May be present None
            return None
        return ival

    @property
    def publication_day(self):
        """Original publication day"""
        try:
            val = self._work_dict['original_publication_day']['#text']
            ival = int(val)
        except KeyError:  # May not be present
            return None
        except TypeError:  # May be present None
            return None
        return ival

    @property
    def publication_date(self):
        """Publication month/day/year for the book"""
        if not self.publication_year:
            return None
        if self.publication_month:
            pub_month = self.publication_month
        else:
            pub_month = 1  # no month specified, default to january
        if self.publication_day:
            pub_day = self.publication_day
        else:
            pub_day = 1  # no day of month specified, default to 1st
        return datetime(year=self.publication_year, month=pub_month, day=pub_day)
