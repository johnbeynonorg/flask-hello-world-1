from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.before_request
def log_details():
    method = request.method
    url = request.url

    @after_this_request
    def log_details_callback(response: Response):
        logger.info(f'method: {method}\n url: {url}\n status: {response.status}')
