# Generated by Django 5.0.3 on 2024-04-02 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='albins_angels',
        ),
    ]