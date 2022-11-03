from django.db import models
import uuid


class InteractionType(models.TextChoices):
    LIKE = "Like"
    DISLIKE = "Dislike"


class Interaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="interactions",
    )
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="interactions",
    )
    date_interaction = models.DateField(auto_now_add=True)
    interaction = models.CharField(
        max_length=30,
        choices=InteractionType.choices,
        default=InteractionType.LIKE,
        null=True,
        blank=True,
    )
