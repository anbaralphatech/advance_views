# Generated by Django 2.1.5 on 2019-02-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quotes', models.TextField()),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
    ]