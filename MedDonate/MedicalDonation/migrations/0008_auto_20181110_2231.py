# Generated by Django 2.1.2 on 2018-11-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalDonation', '0007_auto_20181110_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptor',
            name='end_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='acceptor',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
