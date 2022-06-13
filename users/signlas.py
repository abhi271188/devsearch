from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender = Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('profile saved!')

@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, **kwargs):
    print('Profile deleted')

#post_save.connect(profileUpdated, sender = Profile)
#post_delete.connect(deleteUser, sender=Profile)