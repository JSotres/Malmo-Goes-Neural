from django.urls import path
from .views import SimpsonsGoNeuralApplicationView

urlpatterns = [
    path('simpsons_go_neural/application', SimpsonsGoNeuralApplicationView, name='simpsons_go_neural_application'),
    ]
