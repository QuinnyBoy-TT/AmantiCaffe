# Generated by Django 2.2.6 on 2020-05-07 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20200507_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedule',
            name='staff_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='posts.Staff'),
        ),
    ]