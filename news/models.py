from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    body = models.TextField()
    muallif = models.CharField(max_length=50, verbose_name="Muallif")

    def __str__(self):
        return self.title


class Foot(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ovqat nomi")
    price = models.IntegerField(verbose_name="Narx")

    def __str__(self):
        return self.name

