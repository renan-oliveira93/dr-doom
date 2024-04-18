from django.db import models

class Styles(models.Model):
    primary_color = models.CharField(max_length=6)
    secondary_color = models.CharField(max_length=6)
    tertiary_color = models.CharField(max_length=6)

class Logo(models.Model):
    logo = models.ImageField(upload_to="images/logos%Y/%m/%d", blank=True)

class Customization(models.Model):
    styles = models.ForeignKey(Styles, on_delete=models.CASCADE)
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE)