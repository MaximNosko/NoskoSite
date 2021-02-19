from django.contrib import admin

from .models import News
from .models import Category,Keyword,Comment

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Keyword)
# Register your models here.
