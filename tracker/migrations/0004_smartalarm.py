# Generated by Django 5.1.1 on 2024-11-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_relaxationroutine'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartAlarm',
            fields=[
                ('alarmID', models.AutoField(primary_key=True, serialize=False)),
                ('alarmTime', models.TimeField()),
            ],
        ),
    ]
