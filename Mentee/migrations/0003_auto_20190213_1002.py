# Generated by Django 2.1.5 on 2019-02-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentee', '0002_auto_20190213_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='model_pic',
            field=models.FileField(upload_to='static/img/'),
        ),
    ]