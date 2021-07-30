from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500,default='https://media.istockphoto.com/vectors/illustration-icon-with-the-concept-of-food-donation-vector-id951697932?k=6&m=951697932&s=612x612&w=0&h=cewzX5-oehPnBVufvbWBLbRfvRA_Bh0OouWgHZjzwH0=')

    def __str__(self) -> str:
        return self.item_name 

    def get_absolute_url(self):
        return reverse('food:detail',kwargs={'pk':self.pk})