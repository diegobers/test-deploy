from django.db import models
from django.contrib.auth.models import User
 

class TestModel(models.Model):
    descricao = models.CharField(max_length=200, null=True)
    
    img = models.ImageField(null=True, blank=True, upload_to='img/')  

    def __str__(self):
        return self.descricao 