from django.conf.urls import url
import Autotriage.views.views as publicViews
import Autotriage.views.employee as employeeViews
import Autotriage.views.company as companyViews
import Autotriage.views.server as serverViews
import Autotriage.views.branch as branchViews
import Autotriage.views.contact as contactViews
import Autotriage.views.email as emailViews
from django.contrib.auth import views as auth_views

app_name = 'Autotriage'

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

#branch url
urlpatterns += [
    url(r'^company/branch/(?P<company_id>[0-9])/$',
        branchViews.branchList, name='branchList'),
    url(r'^company/(?P<company_id>[0-9])/add_branch$',
        branchViews.addBranch, name='branchAdd'),
    url(r'^company/(?P<company_id>[0-9])/detail/(?P<branch_id>[0-9])/$',
        branchViews.branchDetail, name='branchDetail'),
    url(r'^company/(?P<company_id>[0-9])/delete/(?P<branch_id>[0-9])/$',
        branchViews.deleteBranch, name='deleteBranch'),
    url(r'^company/(?P<company_id>[0-9])/edit/(?P<branch_id>[0-9])$',
        branchViews.editBranch, name='editBranch'),
]

#server
urlpatterns += [
    url(r'^server_list/(?P<branch_id>[0-9])/$',
        serverViews.serverList, name='serverList'),
    url(r'^server/(?P<branch_id>[0-9])/add$',
        serverViews.addServer, name='serverAdd'),
    url(r'^server/(?P<branch_id>[0-9])/detail/(?P<server_id>[0-9])/$',
        serverViews.serverDetail, name='serverDetail'),
    url(r'^server/(?P<branch_id>[0-9])/delete/(?P<server_id>[0-9])/$',
        serverViews.deleteServer, name='deleteServer'),
    url(r'^server/(?P<branch_id>[0-9])/edit/(?P<server_id>[0-9])$',
        serverViews.editServer, name='editServer'),
]


#contacts
urlpatterns += [
    url(r'^contact/(?P<branch_id>[0-9])/$',
        contactViews.contactList, name='contactList'),
    url(r'^contact/(?P<branch_id>[0-9])/add$',
        contactViews.addContact, name='contactAdd'),
    url(r'^contact/detail/(?P<contact_id>[0-9])/$',
        contactViews.contactDetail, name='contactDetail'),
    url(r'^contact/(?P<branch_id>[0-9])/delete/(?P<contact_id>[0-9])/$',
        contactViews.deleteContact, name='deleteContact'),
    url(r'^contact/(?P<contact_id>[0-9])/edit$',
        contactViews.editContact, name='editContact'),
]

#emails
urlpatterns += [
    url(r'^email/$',
        emailViews.emailList, name='emailList'),
    url(r'^email/add$',
        emailViews.addEmail, name='emailAdd'),
    url(r'^email/detail/(?P<id>[0-9])/$',
        emailViews.emailDetail, name='emailDetail'),
    url(r'^email/delete/(?P<id>[0-9])/$',
        emailViews.deleteEmail, name='deleteEmail'),
    url(r'^email/(?P<id>[0-9])/edit$',
        emailViews.editEmail, name='editEmail'),
]

#login views
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'autotriage/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'autotriage/registration/logged_out.html'}, name='logout'),
]

