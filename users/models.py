from email.policy import default
from django.contrib.auth.models import AbstractUser, User
from django.db import models


#  -------------------   Working Model for Checking Subscribed Users ----------------------


class userSubscriptions(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("userSubscriptions_detail", kwargs={"pk": self.pk})
