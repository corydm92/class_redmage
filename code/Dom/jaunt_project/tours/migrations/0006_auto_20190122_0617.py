# Generated by Django 2.1.5 on 2019-01-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_auto_20190119_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]