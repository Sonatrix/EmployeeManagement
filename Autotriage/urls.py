from django.conf.urls import url
import Autotriage.views.views as publicViews
import Autotriage.views.employee as employeeViews
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
