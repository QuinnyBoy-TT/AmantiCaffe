# Generated by Django 2.2.2 on 2020-02-22 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200221_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]