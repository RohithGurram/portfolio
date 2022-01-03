# Generated by Django 4.0 on 2021-12-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('Language_used', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
    ]
