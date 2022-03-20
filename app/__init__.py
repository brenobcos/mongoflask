from flask import Flask

#Flask Factory
def create_app():
    app = Flask(__name__)

    return app