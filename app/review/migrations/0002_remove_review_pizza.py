# Generated by Django 3.2.13 on 2023-06-13 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='pizza',
        ),
    ]
