from django.contrib import admin

# Register your models here.
from todo_list.models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'done'
    list_display_links = 'title',