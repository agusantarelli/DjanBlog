from django.contrib import admin
from blogweb.models import blogPost,Author,comment
# Register your models here.

admin.site.register(blogPost)
admin.site.register(Author)
admin.site.register(comment)
