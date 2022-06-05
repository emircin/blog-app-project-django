from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default="/profile_pics/default-profile.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


