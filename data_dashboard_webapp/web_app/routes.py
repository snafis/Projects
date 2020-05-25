from web_app import app

import json, plotly
from flask import render_template
from web_app.scripts.data import return_figures

@app.route('/')
@app.route('/index')
def index():

    figures = return_figures()

    #plot ids for the html id tag
    ids = [f'figure-{i}' for i, _ in enumerate(figures)]

    #convert plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)

