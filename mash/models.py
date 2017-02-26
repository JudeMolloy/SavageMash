from django.db import models


class People(models.Model):
    image = models.ImageField(upload_to='media/img')
    rating = models.FloatField(default=1400)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
