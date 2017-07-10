from django.conf.urls import url

from .import views

app_name= 'questionnaire'
urlpatterns = [
    url(r'^contactdetails/$', views.contactdetails, name='contactdetails'),
    url(r'^servicedescription/$', views.servicedescription, name='servicedescription'),
    url(r'^serviceowner/$', views.serviceowner, name='serviceowner'),
    url(r'^enduser/$', views.enduser, name='enduser'),
    url(r'^administrative_level/$', views.administrative_level, name='administrative_level'),
    url(r'^area1/$', views.area1, name='area1'),
    url(r'^deliverychannel/$', views.deliverychannel, name='deliverychannel'),
    url(r'^area2/$', views.Area2View.as_view(), name='area2'),
    url(r'^area3/$', views.Area3View.as_view(), name='area3'),
    url(r'^area4/$', views.Area4View.as_view(), name='area4'),
    url(r'^maturity/$', views.maturity, name='maturity'),
    url(r'^accessibility/$', views.accessibility, name='accessibility'),
    url(r'^prefillingform/$', views.prefillingform, name='prefillingform'),
   
    url(r'^servicedelivery/$', views.servicedelivery, name='servicedelivery'),
    url(r'^service_consumption/$', views.service_consumption, name='service_consumption'),
    url(r'^reuse_and_sharing/$', views.reuse_and_sharing, name='reuse_and_sharing'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/score/$', views.score, name='score'),
    url(r'^initialize/$', views.initialize, name='initialize'),
]
