# Generated by Django 3.0.7 on 2020-09-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_watcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchitem',
            name='item_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
