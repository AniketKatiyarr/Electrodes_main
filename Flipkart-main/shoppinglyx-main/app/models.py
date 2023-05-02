from django.db import models

# Create your models here.

class product(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    pass1 = models.CharField(max_length=50,default="")
    pass2 = models.CharField(max_length=50,default="")
        
    def __str__(self):
        return self.name
    