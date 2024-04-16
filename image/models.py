from django.db import models
from datetime import datetime

class Image(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    credits = models.CharField(max_length=100, null=False, blank=False)
    picture_date = models.DateTimeField(default=datetime.now, blank=False)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d", blank=True)
    
    def __str__(self):
        return self.title