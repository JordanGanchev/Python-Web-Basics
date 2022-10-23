# Generated by Django 4.1.1 on 2022-10-05 18:25

from django.db import migrations, models
import models_demos.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_alter_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(validators=[models_demos.common.validators.validate_in_the_past]),
        ),
    ]
