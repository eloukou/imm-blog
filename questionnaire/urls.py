from django.conf.urls import url

from .import views

app_name= 'questionnaire'
urlpatterns = [
    url(r'^contactdetails/$', views.contactdetails, name='contactdetails'),
    url(r'^servicedescription/$', views.servicedescription, name='servicedescription'),
    url(r'^serviceowner/$', views.serviceowner, name='serviceowner'),
    url(r'^enduser/$', views.enduser, name='enduser'),
    url(r'^administrativelevel/$', views.administrativelevel, name='administrativelevel'),
    url(r'^area1/$', views.area1, name='area1'),
    url(r'^deliverychannel/$', views.deliverychannel, name='deliverychannel'),
    url(r'^area2/$', views.Area2View.as_view(), name='area2'),
    url(r'^area3/$', views.Area3View.as_view(), name='area3'),
    url(r'^area4/$', views.Area4View.as_view(), name='area4'),
    url(r'^maturity/$', views.maturity, name='maturity'),
    url(r'^accessibility/$', views.accessibility, name='accessibility'),
    url(r'^prefillingform/$', views.prefillingform, name='prefillingform'),
   
    url(r'^servicedelivery/$', views.servicedelivery, name='servicedelivery'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/score/$', views.score, name='score'),
    
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<area_id>[0-9]+)/$', views.detail, name='detail'),
    
    
    #url(r'^$', views.place, name='place'), 
   # url(r'^$', views.post_list, name='post_list'),
   # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
   # url(r'^post/new/$', views.post_new, name='post_new'),
   # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), 
 #url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    #url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
   # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
   # url(r'^$', views.dashboard, name='dashboard'), 
]
