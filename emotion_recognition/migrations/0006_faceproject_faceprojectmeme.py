# Generated by Django 3.0.5 on 2020-04-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_recognition', '0005_faceproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='faceproject',
            name='faceProjectMeme',
            field=models.ImageField(blank=True, upload_to='project_description_images'),
        ),
    ]