from flask import Flask

def create_app():
    app = Flask(name)

    @app.route("/v1/hello-world-25")
    def hello():
        return "Hello World 25!"

    return app

