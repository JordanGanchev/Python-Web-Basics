# Generated by Django 4.1.1 on 2022-10-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee_last_name_alter_employee_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]
