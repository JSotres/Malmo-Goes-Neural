# Generated by Django 3.0.5 on 2020-04-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0007_auto_20200416_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description2',
            field=models.TextField(blank=True, default='short description2'),
        ),
    ]