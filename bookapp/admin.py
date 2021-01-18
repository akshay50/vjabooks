from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','sellingprice','offer','codcharge','stock','comingsoon']

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(CompetitionExam)
admin.site.register(Category)