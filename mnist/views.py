from django.shortcuts import render
from django.http import JsonResponse
import re
import os
import base64
from PIL import Image
from io import BytesIO
from .models import mnistProject
import cv2
from .local_python_scripts import ev_digit

def mnistApplicationView(request):
	mnistProjectEx = mnistProject.objects.get(pk=1)
	if request.method == "POST":
		canvasImage = request.POST.get('canvasImage')
		base64_data = re.sub('^data:image/.+;base64,', '', canvasImage)
		byte_data = base64.b64decode(base64_data)
		image_data = BytesIO(byte_data)
		img = Image.open(image_data)
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		savestring = BASE_DIR + '/media/digits/temp.png'
		img.save(savestring)
		predicted_number = ev_digit(savestring)
		response = str(predicted_number)
		return JsonResponse({"output": response})
	return render(request, 'mnist_application.html',
            {'mnistProjectEx': mnistProjectEx})
