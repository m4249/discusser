# Creating database table 
from django.db import models

# Create your models here.
class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    # when first saved not everytime 
    updated = models.DateTimeField(auto_now = True)  
    #  snapshot on ever item we saved
    created = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.name

    