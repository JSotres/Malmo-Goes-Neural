# Generated by Django 3.0.5 on 2020-04-17 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpsons_go_neural', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SimpsonCharacters',
            new_name='SimpsonCharacter',
        ),
    ]
