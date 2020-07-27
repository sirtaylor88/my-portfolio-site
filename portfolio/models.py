from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Publication(models.Model):
    title            = models.CharField(max_length = 256)
    description      = models.TextField()
    authors          = ArrayField(models.CharField(max_length = 30))
    publisher        = models.CharField(max_length = 120)
    publication_date = models.DateField()
    link             = models.CharField(max_length = 120)
    cover_image      = models.ImageField(blank = True,
                                         upload_to = "images")

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self):
        return self.title

    def get_authors(self):
        return ", ".join(self.authors)
