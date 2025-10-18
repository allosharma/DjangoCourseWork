from django.db import models
from uuid_extensions import uuid7

class Product(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=uuid7,  # correct usage
        editable=False
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    thumbnail_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
