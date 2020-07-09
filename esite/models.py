from django.db import models
from django.conf import settings
# Create your models here.

User=settings.AUTH_USER_MODEL


class Item(models.Model):

    catchoices=(
        ("f","fruits"),
        ("v", "vegitables"),
        ("j", "juice"),
    )
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100 , choices=catchoices)
    offer = models.BooleanField(default=False)
    offer_percentage = models.IntegerField()
    offer_price = models.IntegerField()

    def __str__(self):
        return self.name



