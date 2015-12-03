"""project URL Configuration

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
import debug_toolbar
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dvd_list/$', 'main.views.dvd_list'),
    url(r'^dvd_search/$', 'main.views.dvd_search'),
    url(r'^dvd_detail/(?P<pk>\d+)/$', 'main.views.dvd_detail'),
    url(r'^dvd_directory/$', 'main.views.dvd_directory'),
    url(r'^dvd_direct/(?P<char>[^ ])/$', 'main.views.dvd_direct'),
    url(r'^dvd_list_postgres/$', 'main.views.dvd_list_postgres'),
    url(r'^dvd_list_mysql/$', 'main.views.dvd_list_mysql'),
    url(r'^dvd_list_cass/$', 'main.views.dvd_list_cass'),
    url(r'^dvd_detail_postgres/(?P<pk>\d+)/$', 'main.views.dvd_detail_postgres'),
    url(r'^dvd_detail_cass/(?P<pk>\d+)/$', 'main.views.dvd_detail_cass'),
    url(r'^dvd_detail_mysql/(?P<pk>\d+)/$', 'main.views.dvd_detail_mysql'),



    url(r'^__debug__/', include(debug_toolbar.urls)),

]
