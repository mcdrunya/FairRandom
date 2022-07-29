from uuid import uuid4
from django.db import models

class ApplicationRandomModel(models.Model):
    date_open = models.DateTimeField(null=False)
    date_close = models.DateTimeField(null=False)
    _range = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(null=True)
    generated_amount = models.PositiveIntegerField(null=False)
    unique_url = models.CharField(max_length=255, blank=True, null=True)

    # def __str__(self):
    #     return self.
    
