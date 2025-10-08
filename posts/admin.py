from django.contrib import admin
from .models import Post , Author
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title" , "content" , "created_at" , "id"]
    ordering = ["-id"]

admin.site.register(Author)