from django.conf.urls import url
import Autotriage.views.views as publicViews
import Autotriage.views.employee as employeeViews
import Autotriage.views.company as companyViews
import Autotriage.views.server as serverViews
from django.contrib.auth import views as auth_views

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

#server
urlpatterns += [
    url(r'^server_list/(?P<company_id>[0-9])/(?P<is_branch>[0-1])/$',
        serverViews.serverList, name='serverList'),
    url(r'^server_add/(?P<company_id>[0-9])/(?P<is_branch>[0-1])$',
        serverViews.addServer, name='serverAdd'),
    url(r'^server/(?P<company_id>[0-9])/(?P<is_branch>[0-1])/(?P<server_id>[0-9])/$',
        serverViews.serverDetail, name='serverDetail'),
    url(r'^server_delete/(?P<company_id>[0-9])/(?P<is_branch>[0-1])/(?P<server_id>[0-9])/$',
        serverViews.deleteServer, name='deleteServer'),
    url(r'^server_edit/(?P<company_id>[0-9])/(?P<is_branch>[0-1])/(?P<server_id>[0-9])$',
        serverViews.editServer, name='editServer'),
]


#contacts


#login views
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'autotriage/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'autotriage/registration/logged_out.html'}, name='logout'),
]
