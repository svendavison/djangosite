# Generated by Django 3.0.3 on 2020-08-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatisnew',
            name='Image_Two',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/announcements/what_is_new/'),
        ),
    ]