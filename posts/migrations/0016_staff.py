# Generated by Django 2.2.6 on 2020-05-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200405_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_address', models.EmailField(max_length=64)),
                ('staff_number', models.IntegerField()),
            ],
        ),
    ]
