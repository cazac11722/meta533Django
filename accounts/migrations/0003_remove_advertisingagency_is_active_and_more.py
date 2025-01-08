# Generated by Django 5.1.4 on 2025-01-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_advertiser_name_customuser_contact_person_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisingagency',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.CharField(default=True, max_length=255, null=True, verbose_name='진행 여부'),
        ),
    ]
