import os
import time

from keras._tf_keras.keras.preprocessing import image
import numpy as np

from PIL import Image

SIZE = 240


def image_adapt(image_path, output_folder):
    background_color = (0, 0, 0)

    if os.path.isfile(image_path):
        try:
            img = Image.open(image_path)
            img = img.convert("RGB")

            max_dim = max(img.size)
            new_img = Image.new("RGB", (max_dim, max_dim), background_color)
            new_img.paste(img, ((max_dim - img.size[0]) // 2, (max_dim - img.size[1]) // 2))

            new_img = new_img.resize((SIZE, SIZE), Image.LANCZOS)

            unique_id = str(int(time.time()))
            filename = os.path.basename(image_path)
            output_filename = f"{os.path.splitext(filename)[0]}_{unique_id}.jpg"

            os.makedirs(output_folder, exist_ok=True)

            output_path = os.path.join(output_folder, output_filename)
            new_img.save(output_path)

            img.close()
            new_img.close()
            os.remove(image_path)

            return output_path

        except Exception as e:
            raise ValueError(f"Can't open image {image_path}. Error: {e}")

    else:
        raise FileNotFoundError(f"File {image_path} not found.")


def preprocess_image_for_predict(image_path, target_size=(SIZE, SIZE)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

