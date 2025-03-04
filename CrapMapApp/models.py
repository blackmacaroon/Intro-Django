from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class CrapMapApp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="default subtitle", blank=True)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

class PersonalNote(CrapMapApp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)