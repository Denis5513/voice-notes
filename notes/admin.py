from django.contrib import admin
from .models import Tag, UserTag, Note

# Регистрация модели Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)

# Регистрация модели UserTag
class UserTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)

admin.site.register(UserTag, UserTagAdmin)

# Регистрация модели Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'deadline', 'priority', 'record')
    search_fields = ('name',)
    list_filter = ('priority', 'created_at', 'deadline')

admin.site.register(Note, NoteAdmin)