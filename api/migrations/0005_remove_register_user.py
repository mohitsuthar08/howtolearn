# Generated by Django 3.0.6 on 2021-05-04 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='user',
        ),
    ]
