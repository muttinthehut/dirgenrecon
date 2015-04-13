from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from cidtracker import views

router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet)
# router.register(r'groups',views.GroupViewSet)
router.register(r'campaigns',views.MarketingCampaignViewSet)
router.register(r'campaigntypes',views.CampaignTypeViewSet)
router.register(r'marketingchannels',views.MarketingChannelViewSet)
router.register(r'marketingcreatives',views.MarketingCreativeViewSet)
router.register(r'audiencetargetings',views.AudienceTargetingViewSet)
router.register(r'adnetworks',views.AdNetworkViewSet)
router.register(r'marketinggeos',views.MarketingGeoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dirgenrecon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cidtracker/',include('cidtracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
)
