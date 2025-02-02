from django.contrib import admin
from myapp.models import Category, Product  
from myapp.models import YourModel  

class ProductInline(admin.TabularInline):  
    model = Product
    extra = 1  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)
    ordering = ('name',)  
    inlines = [ProductInline]  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  
    search_fields = ('name',)  
    ordering = ('name',)  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('category',) 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('category',)  





class ProductTagInline(admin.StackedInline):
    model = Product.tags.through 
    extra = 1  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description') 
    search_fields = ('name', 'description')  
    ordering = ('-price',)  
    inlines = [ProductTagInline]  


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductTagInline(admin.TabularInline):  
    model = Product.tags.through
    extra = 1




@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',) 
