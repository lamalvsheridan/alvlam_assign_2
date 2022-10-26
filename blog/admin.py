from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    prepopulated_fields = {'slug': ('title',)}

# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
