from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUser
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=CustomUser)
def user_created(sender, created, instance, **kwargs):
    if created:
        Token.objects.create(user=instance)
