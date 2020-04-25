from django.urls import path
from .views import mnistApplicationView

urlpatterns = [
    path('mnist/application/', mnistApplicationView, name='mnist_application'),
    ]