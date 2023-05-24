# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, Flask
from flask_login import login_required
from jinja2 import TemplateNotFound
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import psycopg2
import os
from sqlalchemy.orm import sessionmaker
import requests
import json
from apps.authentication.models import Resources
from sqlalchemy import or_
from flask_msearch import Search
from apps.authentication.models import Post
from flask import current_app



# don't touch this 
@blueprint.route('/index')
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/climate-change-info.html')
def climate_change_info():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=1).all()
    return render_template('home/climate-change-info.html', results=results)

@blueprint.route('/global-aviation-impact.html')
def global_aviation_impact():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=2).all()
    return render_template('home/global-aviation-impact.html', results=results)

@blueprint.route('/climate-economics.html')
def climate_economics():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=3).all()
    return render_template('home/climate-economics.html', results=results)

@blueprint.route('/alternatives-to-traditional-aviation.html')
def alternatives_to_traditional_aviation():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=4).all()
    return render_template('home/alternatives-to-traditional-aviation.html', results=results)

@blueprint.route('/carbon-information.html')
def carbon_info():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=5).all()
    return render_template('home/carbon-information.html', results=results)

@blueprint.route('/airport-sustainability.html')
def airport_sustainability():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=6).all()
    return render_template('home/airport-sustainability.html', results=results)

@blueprint.route('/faa-guidance.html')
def faa_guidance():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=7).all()
    return render_template('home/faa-guidance.html', results=results)

@blueprint.route('/policy-surveys-opposition.html')
def policy_surveys_opposition():
    results=[]
    results = Resources.query.with_entities(Resources.title, Resources.website).filter_by(topic_group=8).all()
    return render_template('home/policy-surveys-opposition.html', results=results)


    
# @blueprint.route("/search", methods=["GET","POST"])
# def search():
#     """
#     1. Capture the word that is being searched
#     2. Search for the word on Google and display results
#     """
#     args = request.args.get("q")
#     return redirect(f'https://google.com/search?q={args}')


# @blueprint.route("/search2", methods=['GET','POST'])
# def search1():
#     if request.method == 'POST':
#         # get search keyword entered by user
#         keyword = request.form["keyword"]

#         # search database
#         #gra_results = Resources.query.with_entities(Resources.title, Resources.website).filter(Resources.topic_title.ilike(f"%{keyword}%",))
#         gra_results = Resources.query.filter(Resources.title.ilike(f'%{keyword}%')).all()

#         # search google
#         #goog_results = list(search(keyword, num_results=10, api_key=os.get_env('YOUR_API_KEY'), cx=os.get_env('YOUR_SEARCH_ENGINE_ID_ACRP')))
#         goog_results = list(search(keyword, num_results=10))

#         # combine results
#         results = []
#         for rec in gra_results:
#             results.append({'title':rec.title, 'website':rec.website})
#         for url in goog_results:
#             results.append({'title': url, 'url': url})

#         return render_template("search-results2.html", keyword=keyword, results=results)

#     return render_template("search2.html")


###this is the code that is good I think, or almost good
# @blueprint.route('/search-home', methods=['GET','POST'])
# def search():
#     query = request.form['query']
#     results = perform_google_search(query)
#     return render_template('search-results2.html', query=query, results=results)

# def perform_google_search(query):
#     api_key = os.getenv('YOUR_API_KEY')
#     search_engine_id = os.getenv('YOUR_SEARCH_ENGINE_ID_ACRP')
#     url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'

#     response = requests.get(url)
#     data = response.json()

#     if 'items' in data:
#         results = data['items']
#         return results

#     return []


@blueprint.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'
        # Detect the current page
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment

    except:
        return None
