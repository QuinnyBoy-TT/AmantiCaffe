# Generated by Django 2.2.2 on 2020-02-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='item_category',
            field=models.CharField(default=True, max_length=100),
        ),
    ]