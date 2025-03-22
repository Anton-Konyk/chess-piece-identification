from flask import Flask
import tensorflow as tf

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"

cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "save_at_56.keras")



if __name__ == '__main__':
    app.run()
