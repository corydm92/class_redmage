# Generated by Django 2.1.5 on 2019-01-18 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyfitness_app', '0002_auto_20190117_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['name']},
        ),
    ]
