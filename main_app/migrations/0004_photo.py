# Generated by Django 2.2 on 2019-06-19 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190619_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Site')),
                ('submission', models.ManyToManyField(to='main_app.Submission')),
            ],
        ),
    ]