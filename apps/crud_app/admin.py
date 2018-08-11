from django.contrib import admin
from .models import Post,Category,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_who_published', 'date_published','description')
    search_fields = ('title', 'user_who_published')

admin.site.register(Post, PostAdmin)
#this line ads new table UI and new entity totally in django admin

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_commented','description',)

admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)