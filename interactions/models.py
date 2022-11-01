from django.db import models
import uuid


class InteractionType(models.TextChoices):
    DEFAULT = "No interaction"
    LIKE = "Like"
    DISLIKE = "Dislike"


class Interaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    date_interaction = models.DateField(auto_now_add=True)
    interaction = models.CharField(
        max_length=30,
        choices=InteractionType.choices,
        default=InteractionType.DEFAULT,
        null=True,
        blank=True,
    )
