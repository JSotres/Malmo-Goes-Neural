from django.db import models


class SimpsonsProject(models.Model):
	simpsonsProjectTextInput = models.TextField(
		blank=True,
		default='faceProjectTextInput'
		)
	simpsonsProjectTextEvaluation = models.TextField(
		blank=True,
		default='faceProjectTextEvaluation'
		)
	simpsonsMeme = models.ImageField(
		upload_to='project_description_images',
		blank=True)
	def __str__(self):
		p = str(self.pk)
		return p


class SimpsonCharacter(models.Model):
    simpson_input_picture = models.ImageField(
        upload_to='simpsonCharacter/simpsonInputPictures/',
        default='simpsonCharacter/simpsonInputPictures/simpsons.jpeg',
        blank=True)
    simpson_output_picture = models.ImageField(
        upload_to='simpsonCharacter/simpsonOutputPictures/',
        default='simpsonCharacter/simpsonOutputPictures/simpsons.jpeg',
        blank=True)
    simpson_evaluated = models.BooleanField(default=False)
    def __str__(self):
    	p = str(self.pk)
    	return p
