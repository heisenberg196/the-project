# Generated by Django 3.2 on 2021-04-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, default='team-3.jpg', null=True, upload_to='images/'),
        ),
    ]
