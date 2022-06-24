from django.contrib.auth.model import User
from iwriter.models import PostRequests
from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PostRequests.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)