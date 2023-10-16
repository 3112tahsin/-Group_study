from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from .models import Room, Topic, Message, User

class MessageAdmin(admin.ModelAdmin):
    list_display=('user', 'room', 'body')
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio', 'display_avatar')

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" />', obj.avatar.url)
        else:
            return format_html('<img src="{}" width="50" height="50" />', 'path/to/default/image.png')
    display_avatar.short_description = 'Avatar'
    
class TopicAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class RoomAdmin(admin.ModelAdmin):
    list_display=('host', 'topic', 'name', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)



