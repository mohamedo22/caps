# Generated by Django 4.2.5 on 2024-02-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_rename_admin_admins_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='flats',
            name='mainimage',
            field=models.ImageField(null=True, upload_to='mainimages/'),
        ),
    ]
