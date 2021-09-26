from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    image = models.ImageField(upload_to="content/images")
    link = models.URLField(blank=True)
