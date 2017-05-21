import unittest
from modules.article import Article


class TestArticleADT(unittest.TestCase):

    def test_create(self):
        self.article = Article('12.20.2012', {'main': 'Some title'},
                               [
                                   {'name': 'subject', 'value': 'Surveillance of Citizens by Government',
                                    'is_major': 'Y',
                                    'rank': '1'},
                                   {'name': 'subject', 'value': 'Freedom of the Press', 'is_major': 'Y', 'rank': '2'},
                                   {'name': 'organizations', 'value': 'Supreme Court of Canada', 'is_major': 'N',
                                    'rank': '3'},
                                   {'name': 'glocations', 'value': 'Montreal (Quebec)', 'is_major': 'Y', 'rank': '4'},
                                   {'name': 'glocations', 'value': 'Quebec Province (Canada)', 'is_major': 'N',
                                    'rank': '5'},
                                   {'name': 'persons', 'value': 'Lagace, Patrick (1972- )', 'is_major': 'Y',
                                    'rank': '6'},
                                   {'name': 'subject', 'value': 'Police Brutality, Misconduct and Shootings',
                                    'is_major': 'Y',
                                    'rank': '7'}])

        self.assertEqual('12.20.2012', self.article.pub_date())
        self.assertEqual('Some title', self.article.headline()['main'])

    def test_detecting_places(self):
        self.article = Article('12.20.2012', {'main': 'Some title'},
                               [
                                   {'name': 'subject', 'value': 'Surveillance of Citizens by Government',
                                    'is_major': 'Y',
                                    'rank': '1'},
                                   {'name': 'subject', 'value': 'Freedom of the Press', 'is_major': 'Y', 'rank': '2'},
                                   {'name': 'organizations', 'value': 'Supreme Court of Canada', 'is_major': 'N',
                                    'rank': '3'},
                                   {'name': 'glocations', 'value': 'Montreal (Quebec)', 'is_major': 'Y', 'rank': '4'},
                                   {'name': 'glocations', 'value': 'Quebec Province (Canada)', 'is_major': 'N',
                                    'rank': '5'},
                                   {'name': 'persons', 'value': 'Lagace, Patrick (1972- )', 'is_major': 'Y',
                                    'rank': '6'},
                                   {'name': 'subject', 'value': 'Police Brutality, Misconduct and Shootings',
                                    'is_major': 'Y',
                                    'rank': '7'}])

        self.assertEqual(['Montreal (Quebec)', 'Quebec Province (Canada)'], self.article.places())


if __name__ == '__main__':
    unittest.main()
