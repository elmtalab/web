# Generated by Django 3.0.7 on 2020-06-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webhooktest', '0002_auto_20200619_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='adrress',
            new_name='addrress',
        ),
    ]