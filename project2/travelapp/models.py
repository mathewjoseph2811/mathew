from django.db import models

# Create your models here.
class travel(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return self.name

class person(models.Model):
    name1=models.CharField(max_length=200)
    img1=models.ImageField(upload_to='pictures')
    desc1=models.TextField()

    def __str__(self):
        return self.name1

