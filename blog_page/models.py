from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=332)
    auther = models.CharField(max_length=32)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'