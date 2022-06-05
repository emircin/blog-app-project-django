from django.db import models
from django.utils import timezone
from users.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=250)
    image = models.ImageField(upload_to="images", blank=True, null=True, default='/images/default.png')
    post_date =  models.DateTimeField(auto_now_add=True)
    post_update = models.DateTimeField(auto_now=True)

    CATEGORY =(
        ("1", "Frontend"),
        ("2", "Backend"),
        ("3", "FullStack"),
    )

    category = models.CharField(max_length=50, choices=CATEGORY, default=CATEGORY[0])


    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
