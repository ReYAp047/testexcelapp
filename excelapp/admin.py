from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'qnt', 'price',)  # Add more fields as needed

class ProductImportExportAdmin(ProductAdmin, ImportExportModelAdmin):
    pass

admin.site.register(Product, ProductImportExportAdmin)
