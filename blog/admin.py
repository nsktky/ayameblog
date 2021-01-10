from django.contrib import admin

from blog.models import Category, Tag, Post, ContentImage, Comment, Reply


class ContentImageInLine(admin.TabularInline):
    model = ContentImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInLine,
    ]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)