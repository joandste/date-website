# Generated by Django 2.1.15 on 2020-01-09 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Collection'),
        ),
    ]
