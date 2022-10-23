# Generated by Django 4.1.1 on 2022-10-03 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_remove_accesscard_id_alter_accesscard_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
        ),
    ]
