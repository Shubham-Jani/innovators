from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=10000)

    class Meta:
        db_table = "post"

    def __str__(self) -> str:
        return self.title


class Reply(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

    class Meta:
        db_table = "reply"

    def __str__(self) -> str:
        return self.description
