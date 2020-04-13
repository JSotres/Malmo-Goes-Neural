from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from .forms import FaceForm
from .models import FaceMood, FaceProject
from .local_python_scripts import ev_mood


class EmotionRecognitionExplanationView(ListView):
    template_name = 'emotion_recognition.html'
    model = FaceProject


def EmotionRecognitionApplicationView(request):
    if request.method == "POST":
        form = FaceForm(request.POST, request.FILES)
        if form.is_valid():
            faceEx = FaceMood()
            faceEx.face_input_picture = request.FILES['face_input_picture']
            faceEx.save()
            faceEx.face_output_picture = ev_mood(faceEx.face_input_picture.url, faceEx.pk)
            faceEx.save()
            return redirect('emotion_evaluated', pk=faceEx.pk)
    else:
        form = FaceForm()
    return render(request, 'emotion_recognition_application.html', {'form': form})


def EmotionEvaluatedView(request, pk):
    faceEx = get_object_or_404(FaceMood, pk=pk)
    return render(request, 'emotion_evaluated.html', {'faceEx': faceEx})


