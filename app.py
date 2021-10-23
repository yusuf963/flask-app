from flask import Flask
app = Flask(__name__)
print(__name__)

from controllers import dialogues
from controllers import users
app.register_blueprint(dialogues.router, url_prefix='/api')
app.register_blueprint(users.router, url_prefix='/api')

