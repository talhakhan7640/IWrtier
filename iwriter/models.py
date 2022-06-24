from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class IWriter(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField(100, default=0) #cents

#     def __str__(self):
#         return self.name

#     def get_display_price(self):
#         return "{0:.2f}".format(self.price / 100)


class PostRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_request = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username