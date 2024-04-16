from django.db import models
from image.models import Image

class Post(models.Model):
    CATEGORY_OPTIONS = [
    ("CATEGORIA1","Categoria1"),
    ("CATEGORIA2","Categoria2"),
    ("CATEGORIA3","Categoria3"),
    ("CATEGORIA4","Categoria4"),
    ]
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    published = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    image = models.ForeignKey(
        to=Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="post_image",
    )

    def __str__(self):
        return self.title