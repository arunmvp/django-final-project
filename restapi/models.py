from django.db import models

# Create your models here.

class userinfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name 

    
