import os

import gdown
from flask import Flask, request, render_template, jsonify
import tensorflow as tf

from classifier import image_adapt, predict

app = Flask(__name__)


STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"
MODEL_FOLDER = "static/models/"
MODEL_FILE = os.path.join(MODEL_FOLDER, "model.keras")


url = "https://drive.google.com/uc?export=download&id=1ksHdcgldcuIBomh_dr-8AAysmyaGtX-F"

if not os.path.exists(MODEL_FILE):
    gdown.download(url, MODEL_FILE, quiet=False)

cnn_model = tf.keras.models.load_model(MODEL_FILE)


def clear_upload_folder():
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error while deleting {file_path}: {e}")


@app.route("/")
def index():
    clear_upload_folder()
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def upload_file():
    file = request.files["image"]
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_image_path)

    return jsonify({"message": "File uploaded", "url": f"/static/uploads/{file.filename}"})


if __name__ == '__main__':
    app.run()
