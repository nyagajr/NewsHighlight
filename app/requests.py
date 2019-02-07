import urllib.request, json
from .models import Source, Article

# getting api key
api_key = None

# getting the source base url
base_url = None

# getting the articles base url
base_url2 = None


def configure_request(app):
    global api_key, base_url, base_url2
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url2 =app.config['NEWS_API_BASE_URL2']

def get_source(newss):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(newss,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

