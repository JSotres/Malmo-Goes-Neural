from django.db import models

# Create your models here.
class mnistProject(models.Model):
	mnistProjectTextInput = models.TextField(
		blank=True,
		default='faceProjectTextInput'
		)
	mnistProjectTextEvaluation = models.TextField(
    	blank=True,
		default='faceProjectTextEvaluation'
		)
	mnistMeme = models.ImageField(
		upload_to='project_description_images',
		blank=True)
	def __str__(self):
		p = str(self.pk)
		return p
