# Generated by Django 3.0.7 on 2020-06-22 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0026_auto_20200622_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_projects',
            name='grouping_name_projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='desk_center.grouping_name_projects'),
        ),
    ]
