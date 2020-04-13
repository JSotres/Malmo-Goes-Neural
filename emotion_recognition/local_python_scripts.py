# import the necessary packages
import numpy as np
import cv2
import os
import keras
# from keras.models import load_model
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array



def ev_mood(img, pk):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    # load our serialized model from disk
    prototxt = BASE_DIR + '/emotion_recognition/deploy.prototxt.txt'
    model = BASE_DIR + '/emotion_recognition/res10_300x300_ssd_iter_140000.caffemodel'
    confidence = 0.7
    evaluation_model_path = BASE_DIR + '/emotion_recognition/model_v6_23.hdf5'
    print(evaluation_model_path)

    classifier = load_model(evaluation_model_path)
    emotion_dict= {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
    label_map = dict((v,k) for k,v in emotion_dict.items())
    print('aqui')

    net = cv2.dnn.readNetFromCaffe(prototxt, model)

    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    img = BASE_DIR + img
    image = cv2.imread(img)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the  prediction
        _confidence = detections[0, 0, i, 2]
        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if _confidence > confidence:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            roi2 = image[startY:endY, startX:endX]

            face_image = cv2.resize(roi2, (48,48))
            face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

            roi = face_image.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = classifier.predict(roi)[0]
            predicted_class = preds.argmax()
            predicted_label = label_map[predicted_class]
    
    
            print(predicted_label)

            # draw the bounding box of the face along with the associated
            # probability
            # text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            gray = cv2.putText(image, predicted_label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    savepath = 'emotionrecognition/faceoutputpictures/'
    fullsavepath = BASE_DIR + '/media/emotionrecognition/faceoutputpictures/'
    savestring = fullsavepath + 'output.jpg'
    print(savestring)
    cv2.imwrite(savestring, gray)
    savestring2 = savepath + 'output.jpg'
    return savestring2
