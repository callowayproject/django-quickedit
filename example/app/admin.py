from models import Blog, Entry
from django.contrib import admin
from django.conf import settings

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ['approved', 'public']
    list_display = ('title', 'pub_date','blog', 'public', 'approved')

    search_fields = ('blog__title','title','tease','body')   
    date_hierarchy = 'pub_date'
    
    list_filter = ('blog','public','approved')
    list_editable = ('public', 'approved')
   
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)    
