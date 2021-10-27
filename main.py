from flask import Flask
import pip


def create_app():
    app = Flask(__name__)

    @app.route("/v1/hello-world-25")
    def hello():
        return "Hello World 25!"

    return app
