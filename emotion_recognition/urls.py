from django.urls import path
from .views import EmotionRecognitionApplicationView, EmotionEvaluatedView

urlpatterns = [
    path('emotion_recognition/application', EmotionRecognitionApplicationView, name='emotion_recognition_application'),
    path('emotion_recognition/evaluated/<int:pk>', EmotionEvaluatedView, name='emotion_evaluated'),
    ]
