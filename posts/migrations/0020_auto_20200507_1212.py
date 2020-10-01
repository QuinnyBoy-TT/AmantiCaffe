# Generated by Django 2.2.6 on 2020-05-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_customer_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_address',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_email',
            field=models.EmailField(max_length=64),
        ),
    ]