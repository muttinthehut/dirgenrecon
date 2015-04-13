# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdGroup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adgroup_code', models.CharField(max_length=3, default='')),
                ('adgroup_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdNetwork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('network_code', models.CharField(max_length=3, default='')),
                ('network_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdPlacement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('placement_code', models.CharField(max_length=3, default='')),
                ('placement_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AudienceTargeting',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('targeting_code', models.CharField(max_length=6, default='')),
                ('targeting_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type_code', models.CharField(max_length=3, default='')),
                ('type_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreativeType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('creative_type_code', models.CharField(max_length=3, default='')),
                ('creative_type_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarketingCampaign',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('campaign', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('landingpage', models.CharField(max_length=100)),
                ('trackingcode', models.CharField(max_length=30, blank=True, default='')),
                ('adnetwork', models.ForeignKey(to='cidtracker.AdNetwork')),
            ],
            options={
                'verbose_name': 'marketing campaign',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarketingChannel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('channel_code', models.CharField(max_length=3, default='')),
                ('channel_description', models.CharField(max_length=20, default='')),
            ],
            options={
                'verbose_name': 'Marketing Channel',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarketingCreative',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('creative_code', models.CharField(max_length=6, default='')),
                ('creative_description', models.CharField(max_length=50, default='')),
                ('creative_copy', models.TextField(null=True, max_length=200, blank=True)),
                ('creative_type', models.ForeignKey(to='cidtracker.CreativeType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarketingGeo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('geo_code', models.CharField(max_length=3, default='')),
                ('geo_description', models.CharField(max_length=30, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='channel',
            field=models.ForeignKey(to='cidtracker.MarketingChannel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='creative',
            field=models.ForeignKey(to='cidtracker.MarketingCreative'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='geo',
            field=models.ForeignKey(to='cidtracker.MarketingGeo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='targeting',
            field=models.ForeignKey(to='cidtracker.AudienceTargeting'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='type',
            field=models.ForeignKey(to='cidtracker.CampaignType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='marketingcampaign',
            unique_together=set([('type', 'channel', 'creative', 'targeting', 'adnetwork', 'geo')]),
        ),
    ]
