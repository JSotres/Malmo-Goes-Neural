from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, RequestReceivedPageView, ProjectListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('project_list/', ProjectListView.as_view(), name='project_list'),
    path('request_received/', RequestReceivedPageView.as_view(), name='request_received'),
    ]
