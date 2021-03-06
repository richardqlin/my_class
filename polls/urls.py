"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
#from django.contrib import admin
from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$',views.index, name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^contact_success/$',views.contact_success,name='contact_success'),
    url(r'^list/$',views.list,name='list'),
    url(r'^search/$',views.search,name='search'),
    #url(r'^searchpage/$',views.searchpage,name='searchpage'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^contact_update/$',views.update,name='update'),
    #url(r'^contact_update_success/$',views.contact_update_success,name='contact_update_success'),

	]
    #url(r'^admin/', admin.site.urls),
'''
    url(r'^$',views.IndexView.as_view(), name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
'''

