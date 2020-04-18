from django.db import models

# Create your models here.
class SimpsonCharacter(models.Model):
    simpson_input_picture = models.ImageField(
        upload_to='simpsonCharacter/simpsonInputPictures/', blank=True)
    simpson_output_picture = models.ImageField(
        upload_to='simpsonCharacter/simpsonOutputPictures/', blank=True)

    def __str__(self):
        p = str(self.pk)
        return p
