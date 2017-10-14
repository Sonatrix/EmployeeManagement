from django.contrib import admin
from Autotriage.models import Employee, Company, CompanyServer, Branch,Contact

admin.site.register(Employee);
admin.site.register(Company)
admin.site.register(CompanyServer)
admin.site.register(Branch)
admin.site.register(Contact)
