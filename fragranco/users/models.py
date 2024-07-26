from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo = models.ImageField(
        'Profile image',
        upload_to='users/',
        blank=True, null=True
    )
    status = models.TextField(max_length=300)

    def __str__(self):
        return self.username
