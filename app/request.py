from app import app
import urllib.request,json
from .models import news

Sources= news.Sources

#getting api key
api_key= app.config['NEWS_API_KEY']

#getting the sources base url
base_url = app.config['SOURCES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results =process_results(sources_results_list)


def process_results(source_list):
    '''
    Function that process the source results and transforms the to a list objects

    Args:
        source_list: A list of dictionaries that contains source details

    Returns:
        source_results: A list of source objects
    '''

    source_results =[]
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        descreption = source_item.get('descripotion')
        url = source_item.get('url')
        category = source_item.get('category')

    return source_results


