# Generated by Django 3.0.7 on 2020-10-08 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imrunicorn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecounter',
            options={'ordering': ('page_name', 'page_hit_count')},
        ),
    ]
