from django.db import models

class Data(models.Model):
    number = models.IntegerField(default = 0)
    name = models.CharField(max_length = 20)
    position = models.CharField(max_length = 20)
    hand = models.CharField(max_length = 20)
    birth = models.CharField(max_length = 20)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.number