# Generated by Django 4.1.7 on 2023-05-01 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='cover_letter',
        ),
    ]