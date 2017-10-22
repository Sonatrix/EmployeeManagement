from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Company, CompanyServer, Branch, Contact

admin.site.register(Employee, UserAdmin)
admin.site.register(Company)
admin.site.register(CompanyServer)
admin.site.register(Branch)
admin.site.register(Contact)
