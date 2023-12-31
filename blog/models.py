from django.db import models

# Create your models here.
class Article(models.Model):
    title  = models.CharField(max_length=60)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title[:30]
