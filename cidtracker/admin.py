from django.contrib import admin

# Register your models here.
from cidtracker.models import MarketingCampaign,MarketingChannel,MarketingGeo,AudienceTargeting,AdNetwork,MarketingCreative,CampaignType,CreativeType,AdPlacement,AdGroup
admin.site.register(MarketingCampaign)
admin.site.register(MarketingChannel)
admin.site.register(MarketingGeo)
admin.site.register(AudienceTargeting)
admin.site.register(AdNetwork)
admin.site.register(MarketingCreative)
admin.site.register(CampaignType)
admin.site.register(CreativeType)
admin.site.register(AdPlacement)
admin.site.register(AdGroup)