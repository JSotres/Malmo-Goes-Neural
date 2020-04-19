# import the necessary packages
import numpy as np
import cv2
import os
import keras
# from keras.models import load_model
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array
from tensorflow.keras.models import model_from_json  #load already trained models
from tensorflow.keras.preprocessing import image  #load images easily



def ev_simpson(imagetest, pk):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	print('aqui28')
	print(BASE_DIR)
	print(imagetest)
	imagetest = BASE_DIR + imagetest
	print(imagetest)

	target_names = ['Abraham Grampa Simpson', 'Agnes Skinner', 'Apu Nahasapeemapetilon',
	'Barney Gumble', 'Bart Simpson', 'Brandine Spuckler','Carl Carlson',
	'Charles Montgomery Burns', 'Chief Wiggum', 'Cletus Spuckler','Comic Book Guy',
	'Disco Stu', 'Dolph Starbeam','Duff Man','Edna Krabappel',
	'Fat Tony', 'Gary Chalmers','Gil', 'Groundskeeper Willie', 'Homer Simpson',
	'Jimbo Jones', 'Kearney Zzyzwicz','Kent Brockman', 'Krusty the Vlown',
	'Lenny Leonard', 'Lionel Hutz', 'Lisa Simpson', 'Lunchlady Doris','Maggie Simpson',
	'Marge Simpson', 'Martin Prince', 'Mayor Quimby','Milhouse van Houten',
	'Miss Hoover', 'Moe Szyslak', 'Ned Flanders','Nelson Muntz', 'Otto Mann',
	'Patty Bouvier', 'Principal Skinner', 'Professor John Frink', 'Rainier Wolfcastle',
	'Ralph Wiggum','Selma Bouvier', 'Sideshow Bob', 'Sideshow Mel','Snake Jailbird',
	'Troy Mcclure', 'Waylon Smithers']

	modeljson = BASE_DIR + '/simpsons_go_neural/modelk.json'
	modelweights = BASE_DIR + '/simpsons_go_neural/model_weightsk.h5'
	cascadefile = BASE_DIR + '/simpsons_go_neural/cascade.xml'
	print(modeljson)
	print(modelweights)

	json_file = open(modeljson, 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)
	model.load_weights(modelweights)

	model.compile(loss='categorical_crossentropy',
    	optimizer='Adam',
    	metrics=['accuracy'])

	faceCascade = cv2.CascadeClassifier(cascadefile)
	sz2 = 64  # y pixels
	sz1 = 64  # x pixels

	color1 = cv2.imread(imagetest, cv2.IMREAD_COLOR)
	img = np.array(image.load_img(imagetest, color_mode="grayscale"))
	gray = cv2.cvtColor(color1, cv2.COLOR_BGR2GRAY)
	imgk = np.array(image.load_img(imagetest))
	faces = faceCascade.detectMultiScale(img, 1.02, 8, minSize=(50,50))

	for (x, y, w, h) in faces:
		w1=int(1.0*w)
		h1 = int(h+0.2*y)
		y1=int(y-0.1*y)
		fc = imgk[y1:y1+h1, x:x+w1]

		roi1 = cv2.resize(fc, (sz2, sz1))
		roi2 = roi1/255.
		roi3 = np.expand_dims(roi2, axis=0)
		pred = model.predict_classes(roi3, verbose=0)
		cv2.rectangle(color1,(x,y1),(x+w1,y1+h1),(0, 0, 255), 2)
		color1 = cv2.putText(color1, target_names[pred[0]], (x, y1-4),
			cv2.FONT_HERSHEY_TRIPLEX, 0.6, (0, 0, 255), 2)

	savepath = 'simpsonCharacter/simpsonOutputPictures/'
	fullsavepath = BASE_DIR + '/media/simpsonCharacter/simpsonOutputPictures/'
	savestring = fullsavepath + 'output' + str(pk) + '.jpg'
	print(savestring)
	cv2.imwrite(savestring, color1)
	savestring2 = savepath + 'output' + str(pk) + '.jpg'
	return savestring2





    