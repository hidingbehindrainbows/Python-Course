from keras.applications.resnet50 import ResNet50
import os
import numpy as np

# Keras
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define the app
app = Flask(__name__)

model = ResNet50(weights='imagenet')


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    # Preprocessing the idfmage
    image_to_be_predicted = image.img_to_array(img)
    image_to_be_predicted = np.expand_dims(image_to_be_predicted, axis=0)
    image_to_be_predicted = preprocess_input(image_to_be_predicted)
    prediction = model.predict(image_to_be_predicted)
    return prediction


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        result = str(pred_class[0][0][1])               # Convert to string
        return result
    return None


app.run()
