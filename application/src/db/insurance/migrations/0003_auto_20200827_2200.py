# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20200826_1650'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InsurancePolicies',
            new_name='InsurancePolicy',
        ),
    ]
