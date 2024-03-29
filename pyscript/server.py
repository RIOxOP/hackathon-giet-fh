from flask import Flask, request
from flask_cors import CORS
from search_good import is_in_top_domains
from domain_analysis import domain_analysis
from search_bad import is_in_fraud_urls
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/check_url', methods=['POST'])
def check_url():
    url = request.json['url']
    if is_in_top_domains(url):
        return {'score': random.randint(88, 95)}
    elif is_in_fraud_urls(url):
        return {'score': random.randint(5, 25)}
    else:
        return {'score': domain_analysis(url)}

if __name__ == '__main__':
    app.run(port=5000)