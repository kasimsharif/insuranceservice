# Generated by Django 3.0.6 on 2020-08-27 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_auto_20200827_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurancepolicy',
            old_name='amount_assured',
            new_name='amount_insured',
        ),
    ]