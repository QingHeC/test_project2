# Generated by Django 2.1.1 on 2019-06-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0017_auto_20190616_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_historys',
            name='run_work_fullname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_historys',
            name='run_work_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
