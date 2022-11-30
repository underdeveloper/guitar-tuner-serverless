import os
from base64 import b64decode
from flask import Flask,json,render_template,jsonify,Response,request,send_from_directory
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

HTMLFILE = "tuner.html"
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/reports/<path:path>')
def send_report(path):
    return send_from_directory('reports', path)

@app.route('/')
def homepage():
    return render_template(HTMLFILE)

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing was found at this URL.', 404

@app.errorhandler(500)
def page_not_found(e):
    return 'Unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",8080)))