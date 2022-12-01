from django.db import models

# Create your models here.
class Records(models.Model):
    uid = models.CharField('User ID',max_length=255)
    sentance = models.CharField('Text',max_length=255)
    result = models.CharField('Sentiment',max_length=255)
