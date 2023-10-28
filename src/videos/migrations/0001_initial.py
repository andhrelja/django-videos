# Generated by Django 4.2.6 on 2023-10-28 19:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('ratings', models.IntegerField(verbose_name='Ratings')),
                ('category_type', models.CharField(choices=[('ELEMENTARY', 'Elementary School'), ('HIGH', 'High School')], max_length=12, verbose_name='Scholar Seniority')),
                ('category_subtype', models.CharField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4th year'), ('5', '5th year'), ('6', '6th year'), ('7', '7th year'), ('8', '8th year')], max_length=1, verbose_name='Class')),
                ('video', models.FileField(null=True, upload_to=pathlib.PureWindowsPath('C:/Users/AndreaHrelja/Public/django-videos/media'), validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
