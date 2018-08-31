class Config:
    '''
    General configuration parent class
    '''
    NEWS_TOP_HEADLINES = 'https://newsapi.org/v2/top-headlines?country=us&category=business&ap'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True