# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, null=True, blank=True)),
                ('studio', models.CharField(max_length=500, null=True, blank=True)),
                ('released', models.CharField(max_length=500, null=True, blank=True)),
                ('status', models.CharField(max_length=500, null=True, blank=True)),
                ('sound', models.CharField(max_length=500, null=True, blank=True)),
                ('versions', models.CharField(max_length=500, null=True, blank=True)),
                ('price', models.CharField(max_length=500, null=True, blank=True)),
                ('rating', models.CharField(max_length=500, null=True, blank=True)),
                ('year', models.CharField(max_length=500, null=True, blank=True)),
                ('genre', models.CharField(max_length=500, null=True, blank=True)),
                ('aspect', models.CharField(max_length=500, null=True, blank=True)),
                ('upc', models.CharField(max_length=500, null=True, blank=True)),
                ('dvd_release_delete', models.CharField(max_length=500, null=True, blank=True)),
                ('dvd_id', models.IntegerField(null=True, blank=True)),
                ('timestamp', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
