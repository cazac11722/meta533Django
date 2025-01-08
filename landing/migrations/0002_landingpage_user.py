# Generated by Django 5.1.4 on 2025-01-06 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='user',
            field=models.ForeignKey(default=1, help_text='The user who owns this landing page', on_delete=django.db.models.deletion.CASCADE, related_name='landing_pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
