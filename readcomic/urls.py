"""readcomic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from comicreader.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home,name='home'),
    url(r'^login/$',login),
    url(r'^accounts/auth/$',authenticates),
    url(r'^accounts/login_home/$',login_home,name='login_home'),
    url(r'^accounts/invalid/$',invalid),
    url(r'^accounts/register/$',register),
    url(r'^accounts/logout/$',logoutaccount),
    url(r'^accounts/upload/$',upload),
    url(r'^accounts/uploaded/$',uploaded,name='uploaded'),
    url(r'^accounts/success/(?P<i>\d+)/$',regSucsess,name='success'),
    url(r'^accounts/upsuccess/$',upSuccess,name='success2'),
    url(r'^accounts/delete/(\d+)/$',deleteRecord,name='deleteRecord')
    #url(r'^success/$',regSucsess)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

