from django.db import models


class FaceProject(models.Model):
    face_project_tutorial = models.TextField(blank=True)


class FaceMood(models.Model):
    face_input_picture = models.ImageField(
        upload_to='emotionrecognition/faceinputpictures/')
    face_output_picture = models.ImageField(
        upload_to='emotionrecognition/faceoutputpictures/', blank=True)

    def __str__(self):
        p = str(self.pk)
        return p
