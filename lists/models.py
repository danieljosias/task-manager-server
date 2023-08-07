from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

class List(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False)
    title = models.CharField(max_length=255)
    card = ArrayField(models.CharField(max_length=255))

    user = models.ForeignKey('users.User', on_delete = models.CASCADE, related_name = 'lists')
    
    