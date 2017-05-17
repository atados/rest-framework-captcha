import uuid
from django.db import models

class Captcha(models.Model):
  secret = models.CharField(max_length=80)
  uuid = models.UUIDField(default=uuid.uuid4, editable=False)
