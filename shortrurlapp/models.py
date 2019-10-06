from django.db import models

# Create your models here.


class ShortUrls(models.Model):
    url = models.URLField('URL', unique=False)
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.url
