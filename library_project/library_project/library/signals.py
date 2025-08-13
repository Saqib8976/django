from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserLogin

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    UserLogin.objects.create(user=user)
