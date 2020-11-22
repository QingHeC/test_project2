# Generated by Django 2.1.1 on 2019-08-11 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0022_auto_20190704_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='files_save',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=200)),
                ('file_md5', models.CharField(max_length=200)),
                ('update_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
