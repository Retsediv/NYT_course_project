from modules.geolocation import Geolocation
from modules.article import ArticlesProcess, Article
import json

from modules.nytapi import ArchiveAPI
import json

NYT_API_KEY = "edfee37ae9e24f848d39bd3976afa7bd"
GEO_KEYS = [
    "AIzaSyAED-hosDmxN2bkNFEQteHNEcP0SVQebH8",
    "AIzaSyDTdFBLKHB3CygvXpPi-pgnUTip_p2o4PQ",
    "AIzaSyA6RY_IzWA5NbjIpUvaUrjeJmUN4EGSATE",
    "AIzaSyBrezgCSQne1zOLo8mytYDfwGFkrMCsu1k",
    "AIzaSyAZuw48KiSoyD-M02L6RvF8GVEyPYv6MGI",
    "AIzaSyA3J0zIbVcA4wera_zhWEwaOERlMsFFk-A",
    "AIzaSyCaF57Wyn59nBYzMSn10e8CuqDiURb2ZEA",
    "AIzaSyCmvuR3MJFt-H9KQh2gSC5aamNfkLUkNc0",
    "AIzaSyBpDlzvP4ETytbPk3zVYjC3VqXE7lSr7C4",
    "AIzaSyD4LCpJ9ClNaCADy85n8n9VyRO2nCweaeA",
    "AIzaSyAGxTZG7G34sqr-a3sNPKwVYarxNBjk-2g",
    "AIzaSyDr8AapNc0IQvG-RJKYJi7jD_BRD7izHiI",
    "AIzaSyBit41NBregOXu7pVcb-PTl_TEeRrfOKCg"]


def filter_with_geo(article):
    for key in article['keywords']:
        if key['name'] == 'glocations':
            return True

    return False


def clear_articles(articles):
    for article in articles:
        keywords = article["keywords"]
        pub_date = article["pub_date"]
        headline = article["headline"]

        article.clear()

        article["keywords"] = keywords
        article["pub_date"] = pub_date
        article["headline"] = headline

    return articles


counter = 0
for year in range(2006, 2008):
    for month in range(4, 13):
        # Getting articles from NYT API
        api = ArchiveAPI(NYT_API_KEY)
        articles = api.query(year, month)['response']['docs']
        geo_articles = clear_articles(list(filter(filter_with_geo, articles)))

        # Articles processing
        processing = ArticlesProcess()
        for article in geo_articles:
            processing.append(Article(article['pub_date'], article['headline'], article['keywords']))

        data = processing.process()
        result = []

        # Get geolocation for the place
        geo = Geolocation(GEO_KEYS)
        i = 0
        for key in data:
            i += 1
            if i % 100:
                print(i)
            coords = geo.get_geo(key)
            result.append((coords, data[key]))

        # Write results to json file
        with open("../../data/{}-{}.json".format(year, month), "w") as f:
            f.write(json.dumps(result))

        # Printing
        counter += 1
        print("STEP: " + str(counter))
        print("______________________")
