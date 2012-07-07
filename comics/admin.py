#-*- coding: utf-8 -*-

from django.contrib import admin
from models import WebComic, Strip, BlogPage, Points

admin.site.register(WebComic)
admin.site.register(Strip)
admin.site.register(BlogPage)
admin.site.register(Points)
