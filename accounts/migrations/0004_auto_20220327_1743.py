# Generated by Django 3.2.9 on 2022-03-27 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220327_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='current_period_end',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='customer_id',
        ),
    ]