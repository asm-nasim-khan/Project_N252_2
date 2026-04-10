from django.db import models

# # Create your models here.
class All_user(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.fname