import cv2
from tensorflow.keras.models import load_model
import numpy as np
import os

def prepare(file):
    RESIZE = 28
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    img = cv2.bitwise_not(img)
    new_img = cv2.resize(img, (RESIZE, RESIZE)) 
    new_img = new_img/255.
    return new_img.reshape(-1, RESIZE, RESIZE, 1)

def ev_digit(imagetemp):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	model_file = '/mnist/mnist.model'
	model_file = BASE_DIR + model_file
	model = load_model(model_file)
	prepared_image = prepare(imagetemp)
	predicted_label = model.predict(prepared_image)
	predicted_label = np.argmax(predicted_label, axis = 1)
	return(predicted_label[0])




