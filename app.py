from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"



if __name__ == '__main__':
    app.run()
