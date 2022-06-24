from django.contrib import admin
from .models import Room, Topic, Message, Book

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(Book)

