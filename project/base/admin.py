from django.contrib import admin

# Register your models here.
from .models import Room

admin.site.register(Room)  #create room model database in admin section
