import unittest
import json
from modules.article import Article, ArticlesProcess


class TestArticleProcessingADT(unittest.TestCase):
    def test_create(self):
        processor = ArticlesProcess()
        self.assertIsNone(processor._head)

    def test_articles_appending(self):
        data = "[{'pub_date': '2016-11-01T23:57:01Z', 'headline': {'main': 'Montreal Police Face a Storm of Criticism Over Surveillance of a Journalist', 'print_headline': 'Montreal Police Face a Storm of Criticism Over Surveillance of a Journalist'}, 'keywords': [{'name': 'subject', 'value': 'Surveillance of Citizens by Government', 'is_major': 'Y', 'rank': '1'}, {'name': 'subject', 'value': 'Freedom of the Press', 'is_major': 'Y', 'rank': '2'}, {'name': 'organizations', 'value': 'Supreme Court of Canada', 'is_major': 'N', 'rank': '3'}, {'name': 'glocations', 'value': 'Montreal (Quebec)', 'is_major': 'Y', 'rank': '4'}, {'name': 'glocations', 'value': 'Quebec Province (Canada)', 'is_major': 'N', 'rank': '5'}, {'name': 'persons', 'value': 'Lagace, Patrick (1972- )', 'is_major': 'Y', 'rank': '6'}, {'name': 'subject', 'value': 'Police Brutality, Misconduct and Shootings', 'is_major': 'Y', 'rank': '7'}]}, {'pub_date': '2016-11-01T23:56:57Z', 'headline': {'main': 'Jurors’ Questions Hint at Division in Trial on Lane Closings', 'print_headline': 'Jurors’ Questions Hint at Split in Trial Over Lane Closings'}, 'keywords': [{'name': 'subject', 'value': 'George Washington Bridge Scandal (2013)', 'is_major': 'N', 'rank': '1'}, {'name': 'persons', 'value': 'Baroni, Bill', 'is_major': 'Y', 'rank': '2'}, {'name': 'persons', 'value': 'Kelly, Bridget Anne', 'is_major': 'Y', 'rank': '3'}, {'name': 'persons', 'value': 'Wigenton, Susan D', 'is_major': 'N', 'rank': '4'}, {'name': 'persons', 'value': 'Christie, Christopher J', 'is_major': 'Y', 'rank': '5'}, {'name': 'glocations', 'value': 'Newark (NJ)', 'is_major': 'N', 'rank': '6'}, {'name': 'glocations', 'value': 'New Jersey', 'is_major': 'Y', 'rank': '7'}, {'name': 'glocations', 'value': 'George Washington Bridge', 'is_major': 'Y', 'rank': '8'}]}]"
        data = data.replace("'", '"')
        data = json.loads(data.replace('u"', ''))

        processor = ArticlesProcess()
        for article in data:
            processor.append(Article(article['pub_date'], article['headline'], article['keywords']))

        self.assertEqual('Jurors’ Questions Hint at Division in Trial on Lane Closings',
                         processor._head.data.headline()['main'])

    def test_articles_processing(self):
        data = "[{'pub_date': '2016-11-01T23:57:01Z', 'headline': {'main': 'Montreal Police Face a Storm of Criticism Over Surveillance of a Journalist', 'print_headline': 'Montreal Police Face a Storm of Criticism Over Surveillance of a Journalist'}, 'keywords': [{'name': 'subject', 'value': 'Surveillance of Citizens by Government', 'is_major': 'Y', 'rank': '1'}, {'name': 'subject', 'value': 'Freedom of the Press', 'is_major': 'Y', 'rank': '2'}, {'name': 'organizations', 'value': 'Supreme Court of Canada', 'is_major': 'N', 'rank': '3'}, {'name': 'glocations', 'value': 'Montreal (Quebec)', 'is_major': 'Y', 'rank': '4'}, {'name': 'glocations', 'value': 'Quebec Province (Canada)', 'is_major': 'N', 'rank': '5'}, {'name': 'persons', 'value': 'Lagace, Patrick (1972- )', 'is_major': 'Y', 'rank': '6'}, {'name': 'subject', 'value': 'Police Brutality, Misconduct and Shootings', 'is_major': 'Y', 'rank': '7'}]}, {'pub_date': '2016-11-01T23:56:57Z', 'headline': {'main': 'Jurors’ Questions Hint at Division in Trial on Lane Closings', 'print_headline': 'Jurors’ Questions Hint at Split in Trial Over Lane Closings'}, 'keywords': [{'name': 'subject', 'value': 'George Washington Bridge Scandal (2013)', 'is_major': 'N', 'rank': '1'}, {'name': 'persons', 'value': 'Baroni, Bill', 'is_major': 'Y', 'rank': '2'}, {'name': 'persons', 'value': 'Kelly, Bridget Anne', 'is_major': 'Y', 'rank': '3'}, {'name': 'persons', 'value': 'Wigenton, Susan D', 'is_major': 'N', 'rank': '4'}, {'name': 'persons', 'value': 'Christie, Christopher J', 'is_major': 'Y', 'rank': '5'}, {'name': 'glocations', 'value': 'Newark (NJ)', 'is_major': 'N', 'rank': '6'}, {'name': 'glocations', 'value': 'New Jersey', 'is_major': 'Y', 'rank': '7'}, {'name': 'glocations', 'value': 'George Washington Bridge', 'is_major': 'Y', 'rank': '8'}]}]"
        data = data.replace("'", '"')
        data = json.loads(data.replace('u"', ''))

        processor = ArticlesProcess()
        for article in data:
            processor.append(Article(article['pub_date'], article['headline'], article['keywords']))

        self.assertEqual({'Newark (NJ)': 1, 'George Washington Bridge': 1, 'New Jersey': 1, 'Quebec Province (Canada)': 1, 'Montreal (Quebec)': 1},
                         processor.process())

if __name__ == '__main__':
    unittest.main()
