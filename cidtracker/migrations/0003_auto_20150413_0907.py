# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidtracker', '0002_auto_20150409_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adgroup',
            options={'verbose_name': 'Campaign Group'},
        ),
        migrations.AlterModelOptions(
            name='adnetwork',
            options={'verbose_name': 'Ad Network'},
        ),
        migrations.AlterModelOptions(
            name='adplacement',
            options={'verbose_name': 'Placement'},
        ),
        migrations.AlterModelOptions(
            name='audiencetargeting',
            options={'verbose_name': 'Target Audience'},
        ),
        migrations.AlterModelOptions(
            name='campaigntype',
            options={'verbose_name': 'Campaign Type'},
        ),
        migrations.AlterModelOptions(
            name='creativetype',
            options={'verbose_name': 'Creative Type'},
        ),
        migrations.AlterModelOptions(
            name='marketingcampaign',
            options={'verbose_name': 'Marketing Campaign'},
        ),
        migrations.AlterModelOptions(
            name='marketingcreative',
            options={'verbose_name': 'Marketing Creative'},
        ),
        migrations.AlterModelOptions(
            name='marketinggeo',
            options={'verbose_name': 'Geography', 'verbose_name_plural': 'Geographies'},
        ),
        migrations.AlterField(
            model_name='marketingchannel',
            name='channel_description',
            field=models.CharField(max_length=30, default=''),
            preserve_default=True,
        ),
    ]
