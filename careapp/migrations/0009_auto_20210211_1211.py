# Generated by Django 3.1.6 on 2021-02-11 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0008_auto_20210211_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='City',
        ),
    ]
