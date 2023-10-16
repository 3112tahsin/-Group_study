from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

class MessageAdmin(admin.ModelAdmin):
    list_display=('user', 'room', 'body')
    
class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'bio', 'avatar')
    
class TopicAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class RoomAdmin(admin.ModelAdmin):
    list_display=('host', 'topic', 'name', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)



