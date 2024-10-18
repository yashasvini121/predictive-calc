import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image  # Importing PIL for image processing

# Load the model
TF_MODEL_URL = 'https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_asia_V1/1'
LABEL_MAP_URL = 'https://www.gstatic.com/aihub/tfhub/labelmaps/landmarks_classifier_asia_V1_label_map.csv'
IMAGE_SHAPE = (321, 321)
df = pd.read_csv(LABEL_MAP_URL)
label_map = dict(zip(df.id, df.name))

classifier = tf.keras.Sequential([
    tf.keras.layers.InputLayer(shape=IMAGE_SHAPE+(3,)),
    tf.keras.layers.Lambda(lambda x: hub.KerasLayer(TF_MODEL_URL, output_key='predictions:logits')(x))
])

def get_prediction(image):
    # Open the uploaded image file
    img = Image.open(image)
    img = img.resize(IMAGE_SHAPE)  # Resize the image to the expected shape
    img = np.array(img) / 255.0  # Convert to array and normalize
    img = img[np.newaxis, ...]  # Add batch dimension
    prediction = classifier.predict(img)
    return label_map[np.argmax(prediction)]
