from flask import Flask, render_template, request, redirect, url_for, g, make_response

import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#region templates

@app.route("/")
def ROUTE_index():
    return render_template('index.html')

#endregion

#region API endpoints

@app.route("/api/contents",)
def API_get_dir_contents():
    path = request.args.get('path')
    
    if os.path.isdir(path):
        return json.dumps(get_dir_contents(path))
    elif os.path.isfile(path):
        return json.dumps(get_file_contents(path))
    else:
        return make_response(json.dumps({'error':'not found'}), 404)

#endregion

if __name__ == "__main__":
    app.run(debug=True)