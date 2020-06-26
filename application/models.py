from django.db import models


class WebPage(models.Model):
    """
    Parsed WebPage
    """
    url = models.URLField(max_length=2048)
    parsed = models.TextField()
