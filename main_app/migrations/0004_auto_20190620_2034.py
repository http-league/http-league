# Generated by Django 2.2 on 2019-06-20 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190620_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='photo',
        ),
        migrations.AddField(
            model_name='submission',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Photo'),
            preserve_default=False,
        ),
    ]
