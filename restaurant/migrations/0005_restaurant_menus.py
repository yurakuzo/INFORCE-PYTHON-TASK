# Generated by Django 4.0.6 on 2022-08-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menu_day_alter_menu_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menus',
            field=models.ManyToManyField(to='restaurant.menu'),
        ),
    ]
