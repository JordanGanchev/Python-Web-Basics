# Generated by Django 4.1.1 on 2022-10-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=7),
        ),
    ]
