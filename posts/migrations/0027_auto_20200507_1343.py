# Generated by Django 2.2.6 on 2020-05-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20200507_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='shedule_clockin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='shedule',
            name='shedule_clockout',
            field=models.DateTimeField(null=True),
        ),
    ]
