# Generated by Django 2.2 on 2020-01-28 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulations', '0003_auto_20200128_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancehistory',
            name='is_late_attendance',
            field=models.BooleanField(default=False),
        ),
    ]
