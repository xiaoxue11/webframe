from django.db import models

class Goodstype(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    img = models.ImageField(upload_to='home')

    def __str__(self):
        return self.name