from flask import render_template
from app import app
from .request import get_sources


@app.route('/')
def index():

    #getting articles
    source_news =get_sources('technology')
    print(source_news)

    title = 'Home-Welcome to news website'

    return render_template('index.html',title = title, source_news=source_news)








