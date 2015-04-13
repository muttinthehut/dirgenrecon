from django.db import models
import datetime
import mandrill

from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string

# Create your models here.

class MarketingChannel(models.Model):
    channel_code = models.CharField(max_length=3,default='')
    channel_description = models.CharField(max_length=30,default='')
    
    class Meta:
        verbose_name = ("Marketing Channel")

    def __str__(self):
        return self.channel_code + '-' + self.channel_description

class CreativeType(models.Model):
    creative_type_code = models.CharField(max_length=3,default='')
    creative_type_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Creative Type")

    def __str__(self):
        return self.creative_type_code + '-' + self.creative_type_description


class MarketingCreative(models.Model):
    creative_code = models.CharField(max_length=6,default='')
    creative_description = models.CharField(max_length=50,default='')
    creative_type = models.ForeignKey(CreativeType)
    creative_copy = models.TextField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = ("Marketing Creative")

    def __str__(self):
        return self.creative_code + '-' + self.creative_description

class MarketingGeo(models.Model):
    geo_code = models.CharField(max_length=3,default='')
    geo_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Geography")
        verbose_name_plural = ("Geographies")

    def __str__(self):
        return self.geo_code + '-' + self.geo_description

class AudienceTargeting(models.Model):
    targeting_code = models.CharField(max_length=6,default='')
    targeting_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Target Audience")

    def __str__(self):
        return self.targeting_code + '-' + self.targeting_description

class AdNetwork(models.Model):
    network_code = models.CharField(max_length=3,default='')
    network_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Ad Network")

    def __str__(self):
        return self.network_code + '-' + self.network_description

class CampaignType(models.Model):
    type_code = models.CharField(max_length=3,default='')
    type_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Campaign Type")

    def __str__(self):
        return self.type_code + '-' + self.type_description

class AdPlacement(models.Model):
    placement_code = models.CharField(max_length=3,default='')
    placement_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Placement")

    def __str__(self):
        return self.placement_code + '-' + self.placement_description

class AdGroup(models.Model):
    adgroup_code = models.CharField(max_length=3,default='')
    adgroup_description = models.CharField(max_length=30,default='')

    class Meta:
        verbose_name = ("Campaign Group")

    def __str__(self):
        return self.adgroup_code + '-' + self.adgroup_description


class MarketingCampaign(models.Model):
    campaign = models.CharField(max_length=50)
    type = models.ForeignKey(CampaignType)
    channel = models.ForeignKey(MarketingChannel)
    creative = models.ForeignKey(MarketingCreative)
    targeting = models.ForeignKey(AudienceTargeting)
    adnetwork = models.ForeignKey(AdNetwork)
    geo = models.ForeignKey(MarketingGeo)
# jpb, uncomment and migrate to add placement and ad group
    placement = models.ForeignKey(AdPlacement)
    group = models.ForeignKey(AdGroup)
#    period = models.CharField(max_length=30)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True,blank=True)
    landingpage = models.CharField(max_length=100)
    trackingcode = models.CharField(max_length=30,blank=True,default='')

    class Meta:
        verbose_name = "Marketing Campaign"
        unique_together = ("type","channel","creative","targeting","adnetwork","geo","placement","group")

    def save(self,force_insert=False,force_update=False):
        # self.trackingcode = self.channel.channel_code + '.' + self.type.type_code + '.' + self.creative.creative_code + '.' + self.targeting.targeting_code + '.' + self.adnetwork.network_code + '.' + self.geo.geo_code
        # jpb, delete above and uncomment below if you want to add placement and group
        self.trackingcode = self.channel.channel_code + '.' + self.type.type_code + '.' + self.creative.creative_code + '.' + self.placement.placement_code + '.' +self.group.adgroup_code + '.' +self.targeting.targeting_code + '.' + self.adnetwork.network_code + '.' + self.geo.geo_code
        super(MarketingCampaign, self).save(force_insert, force_update)
        # test email only right now
        cid = self
        html_body = render_to_string("client_email.html",locals())
        #print(html_body)
        try:
            mandrill_client = mandrill.Mandrill('ESYomNVo5D661rMsbkz8-w')
            to = [{'email':'joe.burns@directgeneral.com','name':'Joe Burns','type':'to'}]
            # result = mandrill_client.messages.send_raw(raw_message=html_body,from_email='joe.burns@directgeneral.com',from_name='Joe Burns',to=to,async=False,ip_pool='Main Pool',return_path_domain=None)      
            message = {'html':html_body,'subject':'Campaign Identifier Notification','to':to,'from_email':'joe.burns@directgeneral.com','from_name':'Joe Burns'}
            result = mandrill_client.messages.send(message=message,async=False,ip_pool='Main Pool')
        except mandrill.Error:
            print('A mandrill error occurred')
            raise
            
#  >>> c.type.type_code + '.' + c.channel.channel_code + '.' + c.creative.creative_
#  code + '.' + c.targeting.targeting_code + '.' + c.adnetwork.network_code + '.' +
#  c.geo.geo_code

    def __str__(self):
        return self.trackingcode + ' - ' + self.campaign


    
    