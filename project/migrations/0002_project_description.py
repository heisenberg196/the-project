# Generated by Django 3.2 on 2021-04-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=320, null=True, verbose_name='Project Description'),
        ),
    ]