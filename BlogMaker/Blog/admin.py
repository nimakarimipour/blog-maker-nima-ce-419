from django.contrib import admin

from Blog.models import Blog, Comment, Post

admin.site.register(Blog)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog')
    radio_fields = {"blog": admin.VERTICAL}
    date_hierarchy = 'time'
    empty_value_display = '-empty-'
    search_fields = ('title',)
    fields = ('text', 'title', 'summary', 'blog')
