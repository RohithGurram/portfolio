# Generated by Django 4.0 on 2021-12-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_project_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
