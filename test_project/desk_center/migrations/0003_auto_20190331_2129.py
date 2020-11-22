# Generated by Django 2.1.1 on 2019-03-31 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0002_interface_asserts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface_asserts',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='interface_asserts',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]