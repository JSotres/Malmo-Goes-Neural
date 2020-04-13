from django.urls import path
from .views import EmotionRecognitionExplanationView, EmotionRecognitionApplicationView, EmotionEvaluatedView

urlpatterns = [
    path('emotion_recognition/explication', EmotionRecognitionExplanationView.as_view(), name='emotion_recognition'),
    path('emotion_recognition/application', EmotionRecognitionApplicationView, name='emotion_recognition_application'),
    path('emotion_recognition/evaluated/<int:pk>', EmotionEvaluatedView, name='emotion_evaluated'),
    ]
