# Generated by Django 2.0.7 on 2018-12-08 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181207_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member_dtl',
            name='image',
        ),
        migrations.AddField(
            model_name='member_dtl',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member_dtl',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
