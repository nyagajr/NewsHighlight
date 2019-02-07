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
