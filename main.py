from flask import Flask


def create_app():
    app = Flask(__name__)
    app.run()

    @app.route("/v1/hello-world-25")
    def hello():
        return "Hello World 25!"


if __name__ == '__main__':
    app.run()
# return app
