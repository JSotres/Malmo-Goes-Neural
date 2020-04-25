# Generated by Django 3.0.5 on 2020-04-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpsons_go_neural', '0004_simpsonsproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpsoncharacter',
            name='simpson_evaluated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='simpsonsproject',
            name='simpsonsMeme',
            field=models.ImageField(blank=True, upload_to='project_description_images'),
        ),
    ]