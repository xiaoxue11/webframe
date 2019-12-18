from django.db import models
from django.contrib.auth.models import User

class BookInfo(models.Model):
    user = models.ForeignKey(User, verbose_name='account', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default='')
    content = models.TextField(blank=True, default='')
    img = models.ImageField(upload_to='home')

    def __str__(self):
        return self.name

