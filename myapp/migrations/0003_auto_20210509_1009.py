# Generated by Django 3.0.6 on 2021-05-09 04:39

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210509_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_key',
            name='key',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
    ]