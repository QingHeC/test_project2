# Generated by Django 2.1.1 on 2019-05-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0013_task_project_model_task_projects_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_distribution_task',
            name='list_user_info_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_distribution_task',
            name='task_name_name',
            field=models.CharField(default='名字', max_length=255),
            preserve_default=False,
        ),
    ]
