# Generated by Django 2.2 on 2019-06-19 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190619_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='URL',
            new_name='url',
        ),
    ]
