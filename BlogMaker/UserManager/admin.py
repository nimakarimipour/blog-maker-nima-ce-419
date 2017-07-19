from django.contrib import admin
from UserManager.models import UserInfo


@admin.register(UserInfo)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')
    search_fields = ('token',)
    fields = (('user', 'token'), 'current_blog')


admin.register(UsernameAdmin)
