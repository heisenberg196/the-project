# Generated by Django 3.2 on 2021-04-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(default='media/team-3.jpg', upload_to='images/'),
        ),
    ]
