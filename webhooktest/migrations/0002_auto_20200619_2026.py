# Generated by Django 3.0.7 on 2020-06-19 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webhooktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='title',
            new_name='adrress',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='pages',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='fiction',
        ),
    ]