from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=30)
    contentdata = models.TextField()
    createdate = models.DateField()
    readtime=models.IntegerField()

# Create your models here.
