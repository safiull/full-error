# Generated by Django 2.1.3 on 2018-12-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20181207_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member_dtl',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='member_dtl',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]