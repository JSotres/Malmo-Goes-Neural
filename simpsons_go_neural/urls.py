from django.urls import path
from .views import SimpsonsGoNeuralExplanationView, SimpsonsGoNeuralApplicationView

urlpatterns = [
    path('simpsons_go_neural/explication', SimpsonsGoNeuralExplanationView.as_view(), name='simpsons_go_neural'),
    path('emotion_recognition/application', SimpsonsGoNeuralApplicationView.as_view(), name='simpsons_go_neural_application'),
    ]
