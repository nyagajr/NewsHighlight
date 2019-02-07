import os

class Config:
  '''
  general configaration class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
  NEWS_API_KEY = '20a4ff7a91174704b2602d6d1300b154'
  NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/everything?q=apple&from=2019-02-06&to=2019-02-06&sortBy=popularity&apiKey={}'


class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass


class DevConfig(Config):
    '''
    development configuration class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
