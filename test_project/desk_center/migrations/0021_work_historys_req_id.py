# Generated by Django 2.1.1 on 2019-07-04 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0012_autoin_asserts_right_contrast_int'),
        ('desk_center', '0020_work_historys_execute_situation_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_historys',
            name='req_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auto_interface.Req_list_data'),
            preserve_default=False,
        ),
    ]