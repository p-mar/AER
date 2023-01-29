from django.db import models

class Image(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    image = models.ImageField(upload_to='images')

>>>>>>> 9bb8654c0e1fa2d1238491e18278cf49604aa637
=======
    image = models.ImageField(upload_to='images')

>>>>>>> ee9aea8311262ab1ae6a28270a51f7fa736894f5
