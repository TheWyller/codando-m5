from django.db import models
import uuid


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    language = models.ForeignKey("languages.Language", on_delete=models.CASCADE)
    categories = models.ManyToManyField("categories.Category", related_name="posts")
    date = models.DateField(auto_now_add=True)
    url_doc = models.TextField(unique=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    url_logo = models.TextField()
