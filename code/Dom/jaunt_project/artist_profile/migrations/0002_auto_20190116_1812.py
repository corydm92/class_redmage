# Generated by Django 2.1.5 on 2019-01-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]