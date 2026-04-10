from django.db import models
from signup_app.models import All_user

# Create your models here.

# # Create your models here.
class User_post(models.Model):
    email = models.EmailField(max_length=254)
    post_msg = models.CharField(max_length=100)
    cretaed_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.email
    
class Friend_List(models.Model):
    source_friend = models.EmailField(max_length=254)
    target_friend = models.EmailField(max_length=254)
    # des_friend = models.OneToOneField(All_user, on_delete=models.CASCADE)
    cretaed_at = models.DateTimeField(auto_now_add=True)
 