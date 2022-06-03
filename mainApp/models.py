from django.db import models
import uuid

# Create your models here.
class task(models.Model):
    
    id = models.UUIDField(
     primary_key = True,
     default = uuid.uuid4,
     editable = False)
    createdAt = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=200, blank=False, default=None)
    description = models.CharField(max_length=1000, blank=False, default=None)
    email = models.EmailField(blank=False, default=None)

