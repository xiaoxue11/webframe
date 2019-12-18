from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    gender_choice = [
        (0, 'female'),
        (1, 'male'),
    ]
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.BooleanField(choices=gender_choice, default=True)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.name