from django.db import models
from django.urls import reverse
from model_utils import Choices


class Project(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(blank=True, default='short description')
    long_description = models.TextField(blank=True, default='long description')
    project_image = models.ImageField(
        upload_to='project_description_images', blank=True)
    PROJECT_TYPE = Choices('ML & Django', 'Computer_Vision', 'Time_Series', 'Other')
    project_type = models.CharField(
        choices=PROJECT_TYPE,
        default=PROJECT_TYPE.Other,
        max_length=20)
    url = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.name


class ContactRequest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('request_received')
