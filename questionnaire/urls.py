from django.conf.urls import url

from .import views

app_name= 'questionnaire'
urlpatterns = [
    #url(r'^mine/$',  views.area1, name='area1'),
    url(r'^contactdetails/$', views.contactdetails, name='contactdetails'),
    url(r'^servicedescription/$', views.servicedescription, name='servicedescription'),
    url(r'^serviceowner/$', views.serviceowner, name='serviceowner'),
    url(r'^enduser/$', views.enduser, name='enduser'),
    url(r'^administrativelevel/$', views.administrativelevel, name='administrativelevel'),
    #url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
   # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
   # url(r'^$', views.dashboard, name='dashboard'),
   # url(r'^service_context/$', views.service_context, name='service_context'),
    url(r'^servicedelivery/$', views.servicedelivery, name='servicedelivery'),
    
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<area_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/score/$', views.score, name='score'),
    #url(r'^$', views.place, name='place'), 
   # url(r'^$', views.post_list, name='post_list'),
   # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
   # url(r'^post/new/$', views.post_new, name='post_new'),
   # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),  
]
