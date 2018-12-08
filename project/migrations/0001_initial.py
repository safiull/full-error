# Generated by Django 2.1.3 on 2018-12-07 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member_dtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('permanent_add', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('post_date', models.DateTimeField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_address', models.CharField(max_length=33)),
            ],
        ),
        migrations.AddField(
            model_name='member_dtl',
            name='present_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.PresentAddress'),
        ),
    ]
