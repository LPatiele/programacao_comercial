from django.conf.urls import url, include
from autenticacao import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$', auth_views.login, name = 'login'),
    # url(r'^logout/$', auth_views.logout, name = 'logout'),
    url(r'^', include('django.contrib.auth.urls'))
]
