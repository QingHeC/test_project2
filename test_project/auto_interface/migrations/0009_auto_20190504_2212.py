# Generated by Django 2.1.1 on 2019-05-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0008_delete_list_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_list_data',
            name='of_big_model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='req_list_data',
            name='of_big_model_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='req_list_data',
            name='of_big_on_small_model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='req_list_data',
            name='of_big_on_small_model_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]