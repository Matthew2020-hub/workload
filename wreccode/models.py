from django.db import models

# Create your models here.

class Responses(models.Model):
    args = models.JSONField(max_length=12, default={})
    data = models.IntegerField(default=dict)
    file = models.IntegerField( default={})
    form = models.IntegerField(default={})

    def __str__(self):
        return self.form