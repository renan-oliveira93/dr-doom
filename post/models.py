from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title