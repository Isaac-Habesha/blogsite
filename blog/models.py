from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isPublished = models.BooleanField(default=False)
    number_of_views = models.PositiveSmallIntegerField(default=0)
    
