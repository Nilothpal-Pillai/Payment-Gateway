# Generated by Django 3.0.8 on 2020-07-31 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razorpayapp', '0003_auto_20200730_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='razorpayhistory',
            name='payment_mode',
        ),
        migrations.AddField(
            model_name='razorpayhistory',
            name='card_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='razorpayhistory',
            name='card_type',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='razorpayhistory',
            name='name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
