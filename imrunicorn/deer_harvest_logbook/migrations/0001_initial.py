# Generated by Django 3.0.3 on 2020-08-27 23:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loaddata', '0002_handload_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_date', models.DateField(default=datetime.date.today)),
                ('harvest_time', models.TimeField(null=True)),
                ('estimated_weight_lbs', models.DecimalField(decimal_places=2, default=100.25, max_digits=5)),
                ('shot_distance_yards', models.DecimalField(decimal_places=0, default=200, max_digits=4)),
                ('kill_shot', models.ImageField(blank=True, null=True, upload_to='uploads/deer_shots/')),
                ('kill_shot_two', models.ImageField(blank=True, null=True, upload_to='uploads/deer_shots/')),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('UNKNOWN', 'Unknown'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='UNKNOWN', max_length=20)),
                ('firearm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_firearm', to='loaddata.Firearm')),
                ('load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_hand_load', to='loaddata.HandLoad')),
                ('shooter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deer_harvest_logbook_shooter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-harvest_date', 'shooter', 'shot_distance_yards'),
            },
        ),
    ]
