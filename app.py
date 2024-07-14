from flask import Flask, render_template, request, redirect, url_for, g, make_response

import json
import base64
from health_py.query_external_recipes import analyze
from health_py.db_connection import db_connection

conn = db_connection("C:/Users/Jon/Documents/GitHub/HealthyEating/health_py/data/")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#region templates

@app.route("/")
def ROUTE_index():
    return render_template('index.html')

#endregion

#region API endpoints

@app.route("/api/v1/analyze/<url>",)
def API_get_dir_contents(url):
    url = base64.b64decode(url)
    print(f"Analyzing {url}")
    recipe = analyze(url, conn)
    if recipe: # How to test for errors?<
        return make_response(json.dumps(recipe), 200)
    return make_response('Recipe not found', 404)

#endregion

if __name__ == "__main__":
    app.run(debug=True)