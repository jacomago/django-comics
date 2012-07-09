#-*- coding: utf-8 -*-

from django.contrib import admin
from models import WebComic, Strip, BlogPage, Map



# class MapInLine(admin.StackedInline):
#     model = Map
#     extra = 2

# class StripAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('name' {'fields': [ 'name']}),
#         ('script'{'fields': [ 'legend']}),
#         ('strip'{'fields': [ 'image']}),
#         ('tags'{'fields': [ 'tags']}, {'fields': [ 'enable_comments']}),
#         ]
#     inlines = [MapInLine]

#admin.site.register(Strip, StripAdmin)

admin.site.register(WebComic)
admin.site.register(Strip)
admin.site.register(BlogPage)
admin.site.register(Map)
