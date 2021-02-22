# Generated by Django 3.1.6 on 2021-02-08 11:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0002_remove_reg_franchise_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg_franchise',
            name='Pincode',
        ),
        migrations.AddField(
            model_name='reg_franchise',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None),
        ),
    ]
