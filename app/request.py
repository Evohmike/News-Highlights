from .models import Sources, Articles
import urllib.request, json

api_key = None
sources_url = None
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(source_list):
    '''
    Function that process the source results and transforms them to a list objects

    Args:
        source_list: A list of dictionaries that contains source details

    Returns:
        source_results: A list of source objects
    '''

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        if url:
            source_object = Sources(id, name, description, url, category)
        source_results.append(source_object)

    return source_results


def get_articles(source_id, limit):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id, limit, api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])

    return articles_location_results


def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage)
            article_location_list.append(article_source_object)

    return article_location_list


def topheadlines(limit):
    '''
    Function that gets articles based on the source id
    '''
    get_topheadlines_url = topheadlines_url.format(limit, api_key)

    with urllib.request.urlopen(get_topheadlines_url) as url:
        topheadlines_data = url.read()
        topheadlines_response = json.loads(topheadlines_data)

        topheadlines_results = None

        if topheadlines_response['articles']:
            topheadlines_results = process_articles(topheadlines_response['articles'])

    return topheadlines_results


def everything(limit):
    '''
    Function that gets articles based on the source id
    '''
    get_everything_url = everything_url.format(limit, api_key)

    with urllib.request.urlopen(get_everything_url) as url:
        everything_data = url.read()
        everything_response = json.loads(everything_data)

        everything_results = None

        if everything_response['articles']:
            everything_results = process_articles(everything_response['articles'])

    return everything_results


def search_everything(limit, query):
    '''
    Function that looks for articles based on top headlines
    '''
    search_everything_url = everything_search_url.format(query, limit, api_key)
    with urllib.request.urlopen(search_everything_url) as url:
        search_everything_data = url.read()
        search_everything_response = json.loads(search_everything_data)

        search_everything_results = []

        if search_everything_response['articles']:
            search_everything_results = process_articles(search_everything_response['articles'])

    return search_everything_results
