from flask import render_template
from app import app
from .request import get_sources


@app.route('/')
def index():

    #getting general news
    general_news =get_sources('general')
    print(general_news)

    title = 'Home-Welcome to news website'

    return render_template('index.html',title = title, General=general_news)








