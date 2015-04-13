# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidtracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingcampaign',
            name='group',
            field=models.ForeignKey(to='cidtracker.AdGroup', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marketingcampaign',
            name='placement',
            field=models.ForeignKey(to='cidtracker.AdPlacement', default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='marketingcampaign',
            unique_together=set([('type', 'channel', 'creative', 'targeting', 'adnetwork', 'geo', 'placement', 'group')]),
        ),
    ]
