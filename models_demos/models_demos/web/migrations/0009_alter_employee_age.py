# Generated by Django 4.1.1 on 2022-10-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=-1),
        ),
    ]
