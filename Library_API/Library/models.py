# books/models.py

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    
    price = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Books"