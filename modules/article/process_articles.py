import json
from modules.article.node import Node


class ArticlesProcess:
    """ Process an array of articles """

    def __init__(self):
        """
        Create instance of class and set a head of linked structure to None
        """
        self.head = None

    def append(self, article):
        """
        Append article in linked structure

        :param article:
        :return None:
        """
        if self.head is None:
            self.head = Node(article)
        else:
            top = self.head
            top.next = Node(article)

    def process(self):
        """
        Process all articles and return dictionary with frequency of each geolocation

        :return dict:
        """
        freq = {}
        top = self.head

        while top is not None:
            for key_w in top.data.keywords():
                if key_w['name'] == 'glocations':
                    value = key_w['value']
                    if value in freq:
                        freq[value] += 1
                    else:
                        freq[value] = 1

            top = top.next

        return freq

    def process_json(self):
        """
        Return result of articles processing in json format

        :return json:
        """
        return json.dumps(self.process())
