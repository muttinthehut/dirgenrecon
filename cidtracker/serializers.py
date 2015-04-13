from django.contrib.auth.models import User, Group
from cidtracker.models import MarketingCampaign,CampaignType,MarketingChannel,MarketingCreative,AudienceTargeting,AdNetwork,MarketingGeo
#MarketingGeo,AudienceTargeting,AdNetwork
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')

class MarketingCampaignSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.StringRelatedField(read_only=True)
    channel = serializers.StringRelatedField(read_only=True)
    creative = serializers.StringRelatedField(read_only=True)
    targeting = serializers.StringRelatedField(read_only=True)
    adnetwork = serializers.StringRelatedField(read_only=True)
    geo = serializers.StringRelatedField(read_only=True)
# jpb, uncomment below to add ad group and placement
#    group = serializers.StringRelatedField(read_only=True)
#    placement = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MarketingCampaign
        fields = ('campaign','type','channel','creative','targeting','adnetwork','geo','start_date','end_date','landingpage','trackingcode')
# jpb, remove above and uncomment below to add placement and group
#        fields = ('campaign','type','channel','creative','targeting','adnetwork','placement','group','geo','start_date','end_date','landingpage','trackingcode')

class CampaignTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CampaignType
        fields = ('type_code','type_description')

class MarketingChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketingChannel
        fields = ('channel_code','channel_description')

class MarketingCreativeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketingCreative
        fields = ('creative_code','creative_description')

class AudienceTargetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AudienceTargeting
        fields = ('targeting_code','targeting_description')

class AdNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdNetwork
        fields = ('network_code','network_description')

class MarketingGeoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketingGeo
        fields = ('geo_code','geo_description')

# jpb, uncomment below to add AdPlacement and AdGroup
# class AdPlacementSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = AdPlacement
#        fields = ('placement_code','placement_description')

# class AdGroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = AdGroup
#        fields = ('adgroup_code','adgroup_description')