# Generated by Django 2.2.6 on 2020-05-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_no',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
