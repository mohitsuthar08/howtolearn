# Generated by Django 3.0.6 on 2021-05-19 04:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210519_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
