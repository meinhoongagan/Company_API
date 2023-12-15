from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','about','type')
    search_fields=('name','type')
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)