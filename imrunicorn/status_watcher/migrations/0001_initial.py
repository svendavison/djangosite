# Generated by Django 3.0.7 on 2020-09-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(blank=True, null=True)),
                ('item_link', models.TextField(blank=True, null=True)),
                ('item_phrase', models.TextField(blank=True, null=True)),
                ('item_phrase_not_exist', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ('item_name', 'item_phrase'),
            },
        ),
    ]