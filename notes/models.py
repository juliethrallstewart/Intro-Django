from django.db import models
from uuid import uuid4


# id = Default calls a function to randomly generate a unique identifier.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

