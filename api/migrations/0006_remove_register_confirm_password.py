# Generated by Django 3.0.6 on 2021-05-19 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_register_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='confirm_password',
        ),
    ]
