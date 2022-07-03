import email
import profile
from unicodedata import name
from venv import create
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

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
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

        subject = 'Welcome to the DevSearch'
        message = 'We are glad you are here!'

        send_mail (
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently = False)

def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
