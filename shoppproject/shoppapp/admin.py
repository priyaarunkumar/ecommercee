from django.contrib import admin
from . models import Category,Product

# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CatAdmin)

class pdtadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated','slug','description']
    list_editable = ['price','stock','available', 'description']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,pdtadmin)

