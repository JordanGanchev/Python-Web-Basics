# Generated by Django 4.1.2 on 2022-10-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_person_todo_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
