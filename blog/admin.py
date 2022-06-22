from django.contrib import admin
from .models import Post

# Register your models here.

class postInLine(admin.TabularInline):
    model = Post

admin.site.register(Post)
