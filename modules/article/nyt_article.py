class Article:
    """ ADT which represent article from NYT"""

    def __init__(self, pub_date, headline, keywords):
        """
        Create new instance

        :param string pub_date:
        :param dict headline:
        :param list keywords:
        """
        self._pub_date = pub_date
        self._headline = headline
        self._keywords = keywords

    def keywords(self):
        return self._keywords

    def pub_date(self):
        return self._pub_date

    def headline(self):
        return self._headline

    def places(self):
        """
        Find and return all places which are connected with given article

        :return list: list with all places which are connected with given article
        """
        places = []
        for keyw in self._keywords:
            if keyw['name'] == 'glocations':
                places.append(keyw['value'])

        return places
