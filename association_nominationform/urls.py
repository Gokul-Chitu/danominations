"""association_nominationform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as builtinview
from da import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.nominationfields,name='nominationfields'),
    url(r'^accounts/login/$', builtinview.login, name='login'),
    url(r'^dashboard/$', views.registration, name='registrations'),
    # url(r'^dashboard/profile/', ),
    url(r'^dashboard/profile/(?P<pk>\d+)$', views.profile, name='profile'),
    url(r'^dashboard/registrations/$', views.registration, name='registrations'),
    url(r'^dashboard/registrations/president/$', views.presidentview, name='president'),
    url(r'^dashboard/registrations/treasurer/$', views.treasurerview, name='treasurer'),
    url(r'^dashboard/registrations/secretary/$', views.secretaryview, name='secretary'),
    url(r'^dashboard/registrations/joint_secretary/$', views.jointsecretaryview, name='jointsecretary'),
    url(r'^dashboard/report/download/$', views.download, name='download'),
    url(r'^dashboard/report/download/export$', views.export_csv, name='export'),
    url(r'^dashboard/signing_out/$', views.signout, name='signout'),

]
