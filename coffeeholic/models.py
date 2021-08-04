from django.db import models

# Create your models here.


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    website_url = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200)
    memo = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='coffeeshops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
