import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    price = models.IntegerField()  
    description = models.TextField()  
    thumbnail = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
