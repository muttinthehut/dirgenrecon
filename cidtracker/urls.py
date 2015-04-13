from django.conf.urls import patterns, url

from cidtracker import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^new/$',views.marketingcampaign_new,name='marketingcampaign_new'),
    url(r'^list/$',views.marketingcampaign_list,name='marketingcampaign_list'),
    )
