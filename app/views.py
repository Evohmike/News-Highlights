from flask import render_template
from app import app
from .request import get_sources


@app.route('/')
def index():

    #getting general news
    general_news =get_sources('general')
    business_news =get_sources('business')
    entertainment_news =get_sources('entertainment')
    sports_news =get_sources('sports')
    technology_news =get_sources('technology')
    science_news =get_sources('science')
    health_news =get_sources('health')


    print(general_news)

    title = 'Home-Best News Upadate Site'

    return render_template('index.html',title = title, General=general_news,Business=business_news,
                           Entertainment=entertainment_news,Sports=sports_news,Technology=technology_news,
                           Science=science_news,Health=health_news)



@app.route('/articles/<source_id>&<int:per_page>')
def articles(source_id, per_page):
    '''
    Function that returns articles based on their sources
    '''
    # print(source_id)
    # per_page = 40
    news_source = get_articles(source_id, per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title=title, name=source_id, news=news_source)


@app.route('/topheadlines&<int:per_page>')
def headlines(per_page):
    '''
    Function that returns top headlines articles
    '''
    # per_page = 40
    topheadlines_news = topheadlines(per_page)
    title = 'Top Headlines'
    return render_template('topheadlines.html', title=title, name='Top Headlines', news=topheadlines_news)


@app.route('/everything&<int:per_page>')
def all_news(per_page):
    '''
    Function that returns top headlines articles
    '''
    # per_page = 40
    everything_news = everything(per_page)
    title = 'All News'

    search_articles = request.args.get('search_query')

    if search_articles:
        return redirect(url_for('main.search', topic=search_articles))
    else:
        return render_template('topheadlines.html', title=title, name='All News', news=everything_news)


@app.route('/search/<topic>')
def search(topic):
    '''
    function that returns the results of search request
    '''
    limit = 40
    search_name = topic.split(" ")
    search_name_format = "+".join(search_name)
    search_every = search_everything(limit, search_name_format)

    title = '{search_name_format} Results'

    return render_template('search.html', title=title, news=search_every)






