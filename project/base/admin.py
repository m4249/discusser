from django.contrib import admin

# Register your models here.
from .models import Room,Topic,Message,User

admin.site.register(User)
admin.site.register(Room)  #create room model database in admin section
admin.site.register(Topic)
admin.site.register(Message)