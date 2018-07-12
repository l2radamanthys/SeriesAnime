"""SeriesAnime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from Main import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home),
    url(r'^series/$', views.all_serie),
    url(r'^series/(?P<page_>\d+)/$', views.all_serie),
    url(r'^series/completas/$', views.full_serie),
    url(r'^series/completas/(?P<page_>\d+)/$', views.full_serie),
    url(r'^series/incompletas/$', views.empty_serie),
    url(r'^series/incompletas/(?P<page_>\d+)/$', views.empty_serie),
    url(r'^series/ultimas/$', views.last_serie_added),
    url(r'^series/ultimas/(?P<page_>\d+)/$', views.last_serie_added),
    url(r'^series/agregar/$', views.add_serie),
    url(r'^series/agregar-simple/$', views.rapid_add_serie),
    url(r'^series/mostrar/(?P<id_>\d+)/$', views.show_serie),
    url(r'^series/modificar/(?P<id_>\d+)/$', views.edit_serie),
    url(r'^series/eliminar/(?P<id_>\d+)/$', views.delete_serie),
    url(r'^series/agregar-servidor/(?P<id_>\d+)/$', views.add_server_serie),
    url(r'^series/eliminar-servidor/(?P<id_>\d+)/$', views.delete_server_serie),
    url(r'^series/buscar/$', views.search_serie),
]
