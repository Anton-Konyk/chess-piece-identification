import os

from flask import Flask, request, render_template, jsonify
import tensorflow as tf


app = Flask(__name__)


STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"

cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "save_at_56.keras")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def upload_file():
    file = request.files["image"]
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_image_path)

    return jsonify({"message": "File uploaded", "url": f"/static/uploads/{file.filename}"})


if __name__ == '__main__':
    app.run(debug=True)
