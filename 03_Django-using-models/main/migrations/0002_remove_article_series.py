# Generated by Django 4.0.2 on 2022-03-02 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='series',
        ),
    ]
