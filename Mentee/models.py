from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone
from django.db import models as models
# from django.db.models import ImageField

# Create your models here.

class Mentee(models.Model):
    name = models.CharField(max_length=100)
    quotes = models.TextField()
    # model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
