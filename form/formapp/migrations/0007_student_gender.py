# Generated by Django 2.1.5 on 2019-06-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0006_auto_20190625_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='', max_length=100),
        ),
    ]