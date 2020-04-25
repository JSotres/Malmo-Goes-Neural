from django.db import models


class FaceProject(models.Model):
	faceProjectTextInput = models.TextField(
		blank=True,
		default='faceProjectTextInput'
		)
	faceProjectTextEvaluation = models.TextField(
		blank=True,
		default='faceProjectTextEvaluation'
		)
	faceProjectMeme = models.ImageField(
		upload_to='project_description_images',
		blank=True)
	def __str__(self):
		p = str(self.pk)
		return p


class FaceMood(models.Model):
    face_input_picture = models.ImageField(
        upload_to='emotionrecognition/faceinputpictures/', blank=True)
    face_output_picture = models.ImageField(
        upload_to='emotionrecognition/faceoutputpictures/', blank=True)

    def __str__(self):
        p = str(self.pk)
        return p
