from flask import Flask, render_template, request, json, redirect, session
from flask import Markup
import requests

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/")
def main():
    user = {"name":"SURI"}
    return render_template('map.html', user=user,title="Home Page")

@app.route("/map")
@login_required
def map():
    headers = {
        'Authorization': 'Bearer keyMdNcOcmTFobuDZ',
    }
    params = (
        ('view', 'Grid view'),
    )
    r = requests.get('https://api.airtable.com/v0/appcVQeFhB8xzYGa6/STORE?api_key=keyMdNcOcmTFobuDZ', headers=headers, params=params)
    dict = r.json()
    dataset = []
    data = []
    items = {}
    total_entries_list = []
    for i in dict['records']:
         dict = i['fields']
         dataset.append(dict)
    return render_template('map.html', entries = dataset)
