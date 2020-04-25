from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import re
import sys
import os
import base64
from PIL import Image
from io import BytesIO
from django.views.generic import TemplateView
from .models import mnistProject
import cv2
from .local_python_scripts import ev_digit

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fullsavepath = BASE_DIR + '/media/digits/'
savestring = fullsavepath + 'temp.png' 

# @csrf_exempt
def mnistApplicationView(request):
	mnistProjectEx = mnistProject.objects.get(pk=1)

	if request.method == "POST":
		canvasImage = request.POST.get('canvasImage')
		header_len = len('data:image/jpeg;base64,')
		canvasImage[header_len:]
		# image_data = base64.decodebytes(canvasImage)
		# header_len = len('data:image/jpeg;base64,')
		base64_data = re.sub('^data:image/.+;base64,', '', canvasImage)
		byte_data = base64.b64decode(base64_data)
		image_data = BytesIO(byte_data)
		img = Image.open(image_data)
		img.save(savestring)
		# image_data = request.json['image_data'][header_len:].encode()
		# image_data = base64.decodebytes(image_data)
		# with open('temp_image.jpg', 'wb') as f:
			# f.write(image_data)
			# f.close()
		# img2 = cv2.imread(savestring)
		print(savestring)
		predicted_number = ev_digit(savestring)
		# print(predicted_number)
		response = str(predicted_number)
		return JsonResponse({"output": response})
	return render(request, 'mnist_application.html',
            {'mnistProjectEx': mnistProjectEx})
