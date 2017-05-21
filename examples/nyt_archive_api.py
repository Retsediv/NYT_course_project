from modules.nytapi import ArchiveAPI
import json

NYT_API_KEY = "edfee37ae9e24f848d39bd3976afa7bd"


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
for year in range(2010, 2017):
    for month in range(1, 13):
        with open("../data/{}-{}.json".format(year, month), "w") as f:
            api = ArchiveAPI(NYT_API_KEY)
            articles = api.query(year, month)['response']['docs']
            geo_articles = clear_articles(list(filter(filter_with_geo, articles)))

            f.write(json.dumps(geo_articles))

            counter += 1
            print("Step: " + str(counter))
