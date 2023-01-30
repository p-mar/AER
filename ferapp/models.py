from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    video= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.title

class File(models.Model):
    file=models.FileField()
