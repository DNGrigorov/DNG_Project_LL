from django.contrib import admin
from .models import Post, Comment, OriginalPostContent, PostVersion

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(OriginalPostContent)
admin.site.register(PostVersion)
