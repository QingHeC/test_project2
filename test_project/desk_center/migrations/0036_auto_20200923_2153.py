# Generated by Django 3.0.7 on 2020-09-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0035_work_run_request_historys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_assert',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_assert_to',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_headers',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_html',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_param',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='work_run_request_historys',
            name='req_url',
            field=models.TextField(),
        ),
    ]
