from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cidtracker.serializers import UserSerializer, GroupSerializer, MarketingCampaignSerializer,CampaignTypeSerializer
from cidtracker.serializers import MarketingChannelSerializer,MarketingCreativeSerializer,AudienceTargetingSerializer,AdNetworkSerializer,MarketingGeoSerializer

# Create your views here.
from django.http import HttpResponse

from .forms import MarketingCampaignForm
from .models import MarketingCampaign,CampaignType,MarketingChannel,MarketingCreative,AudienceTargeting,AdNetwork,MarketingGeo

def index(request):
    return HttpResponse("Hello World. CID Index")

def marketingcampaign_new(request):
    form = MarketingCampaignForm
    return render(request, 'campaign_edit.html',{'form':form})

def marketingcampaign_list(request):
    marketingcampaigns = MarketingCampaign.objects.all()
    return render(request, 'campaign_list.html',{'marketingcampaigns':marketingcampaigns})


class MarketingCampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed
    """
    queryset = MarketingCampaign.objects.all()
    serializer_class = MarketingCampaignSerializer

class CampaignTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaign type to be viewed
    """
    queryset = CampaignType.objects.all()
    serializer_class = CampaignTypeSerializer

class MarketingChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marketing channel to be viewed
    """
    queryset = MarketingChannel.objects.all()
    serializer_class = MarketingChannelSerializer

class MarketingCreativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marketing creative to be viewed
    """
    queryset = MarketingCreative.objects.all()
    serializer_class = MarketingCreativeSerializer

class AudienceTargetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audience targeting to be viewed
    """
    queryset = AudienceTargeting.objects.all()
    serializer_class = AudienceTargetingSerializer

class AdNetworkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows audience targeting to be viewed
    """
    queryset = AdNetwork.objects.all()
    serializer_class = AdNetworkSerializer

class MarketingGeoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marketing geo locations to be viewed
    """
    queryset = MarketingGeo.objects.all()
    serializer_class = MarketingGeoSerializer