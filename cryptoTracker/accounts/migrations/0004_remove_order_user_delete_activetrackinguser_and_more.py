# Generated by Django 4.0.6 on 2022-07-21 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_activetrackinguser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='ActiveTrackingUser',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
