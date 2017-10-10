from django.conf.urls import url
import Autotriage.views.views as publicViews
import Autotriage.views.employee as employeeViews
import Autotriage.views.company as companyViews
app_name = 'autotriage'

urlpatterns = [
    url(r'^$', publicViews.home, name='home'),
]

#employee views
urlpatterns += [
    url(r'^employee_list/$', employeeViews.employeeList, name='employeeList'),
    url(r'^employee_add$', employeeViews.addEmployee, name='employeeAdd'),
    url(r'^employee/(?P<employee_id>[0-9])/$',
        employeeViews.employeeDetail, name='employeeDetail'),
    url(r'^employee_delete/(?P<employee_id>[0-9])/$',
        employeeViews.deleteEmployee, name='deleteEmployee'),
    url(r'^employee_edit/(?P<employee_id>[0-9])$',
        employeeViews.editEmployee, name='editEmployee'),
]


#company related views
urlpatterns += [
    url(r'^company_list/$', companyViews.companyList, name='companyList'),
    url(r'^company_add$', companyViews.addCompany, name='companyAdd'),
    url(r'^company/(?P<pid>[0-9])/$',
        companyViews.companyDetail, name='companyDetail'),
    url(r'^company_delete/(?P<pid>[0-9])/$',
        companyViews.deleteCompany, name='deleteCompany'),
    url(r'^company_edit/(?P<pid>[0-9])$',
        companyViews.editCompany, name='editCompany'),
]

#branch



#contacts
