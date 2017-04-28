from nytimesarchive import ArchiveAPI


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


with open("data_samples.txt", "w") as f:
    api = ArchiveAPI('edfee37ae9e24f848d39bd3976afa7bd')
    articles = api.query(2016, 11)['response']['docs']
    geo_articles = clear_articles(list(filter(filter_with_geo, articles))[0:2])

    f.write(str(geo_articles))

    print(geo_articles)
