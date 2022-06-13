import email
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
'''
#@receiver(post_save, sender = Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('profile saved!')
'''
'''
#@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, **kwargs):
    print('Profile deleted')
'''
'''
post_save.connect(profileUpdated, sender = Profile)
post_delete.connect(deleteUser, sender=Profile)
'''

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.get(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

post_save.connect(createProfile, sender=User)
