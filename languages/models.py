from django.db import models
import uuid


class Language(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    url_doc = models.TextField(unique=True)
