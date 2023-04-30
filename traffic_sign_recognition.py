import os

import cv2
import keras.models
import numpy as np
from PIL import Image
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)

classes = {
    0: 'Speed limit (20km/h)',
    1: 'Speed limit (30km/h)',
    2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)',
    4: 'Speed limit (70km/h)',
    5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)',
    7: 'Speed limit (100km/h)',
    8: 'Speed limit (120km/h)',
    9: 'No passing',
    10: 'No passing vehicle over 3.5 tons',
    11: 'Right-of-way at intersection',
    12: 'Priority road',
    13: 'Yield',
    14: 'Stop',
    15: 'No vehicles',
}

@app.route('/api/predict', methods=['POST'])
def predict():
    f = request.files['image']
    file_path = secure_filename(f.filename)
    f.save(file_path)
    result = image_recognition(file_path)
    os.remove(file_path)

    return {
        'message': result
    }

def image_recognition(img):
    loaded_model = keras.models.load_model("model/model.h5")

    image = cv2.imread(img)

    image_fromarray = Image.fromarray(image, 'RGB')
    resize_image = image_fromarray.resize((30, 30))
    expand_input = np.expand_dims(resize_image, axis=0)
    input_data = np.array(expand_input)
    input_data = input_data / 255

    pred = loaded_model.predict(input_data)
    result = pred.argmax()
    return classes[result]

if __name__ == "__main__":
    app.run()
