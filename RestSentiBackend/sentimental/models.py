from django.db import models

# Create your models here.
class Records(models.Model):
    uid = models.PositiveIntegerField()
    sentance = models.TextField()
    result = models.BooleanField()

    def __str__(self) -> str:
        return str(self.sentance)
