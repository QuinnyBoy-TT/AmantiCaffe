# Generated by Django 2.2.6 on 2020-05-07 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20200507_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecustomer',
            name='item_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='posts.MenuItem'),
        ),
        migrations.AlterField(
            model_name='onlinecustomer',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]