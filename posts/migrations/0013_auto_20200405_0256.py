# Generated by Django 2.2.2 on 2020-04-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200310_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='description',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='home_address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]