from flask import Flask
app = Flask(__name__)
print(__name__)
@app.route('/')
def home():
    return('hello from flask server', 200)
from controllers import teas
app.register_blueprint(teas.router, url_prefix='/api')