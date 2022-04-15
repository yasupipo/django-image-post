# Generated by Django 3.1 on 2022-03-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='current_period_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='有効期限'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='customer_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客ID'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
