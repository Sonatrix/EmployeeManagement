from django.conf.urls import url
import Autotriage.views as views

app_name = 'autotriage'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
