# Generated by Django 2.1.5 on 2019-06-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(default=False, upload_to='photo/'),
        ),
        migrations.AddField(
            model_name='student',
            name='stream',
            field=models.CharField(choices=[('1', 'CSE'), ('2', 'ECE'), ('3', 'MINING')], default=False, max_length=1),
        ),
        migrations.AddField(
            model_name='student',
            name='video_file',
            field=models.FileField(default=False, max_length=200, upload_to='video/'),
        ),
    ]
