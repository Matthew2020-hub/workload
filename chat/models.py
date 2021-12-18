from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


    class Meta:
        ordering = ('date_created',) 