from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    comment = models.TextField()
    date_comment = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(blank=True, null=True,default=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name='comments')
