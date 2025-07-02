from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    tags = models.CharField(max_length=100, blank=True, null=True)  # 👈 Fix here
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title