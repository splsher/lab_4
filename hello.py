from flask import Flask

app = Flask(__name__)


@app.route('/v1/hello-world-25')
def hello_world():
    return 'Hello World 25 !'


if __name__ == '__main__':
    app.run()