from django.db import models

class GoodsType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='type')

    def __str__(self):
        return self.name
