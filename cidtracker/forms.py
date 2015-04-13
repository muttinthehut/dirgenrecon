from django import forms

from .models import MarketingCampaign

class MarketingCampaignForm(forms.ModelForm):

    class Meta:
        model = MarketingCampaign
        fields = ('campaign','type','channel','creative','targeting','adnetwork','geo','start_date','end_date','landingpage',)


    