# Generated by Django 4.0.6 on 2022-07-25 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0002_remove_tile_category_tile_city_tile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='occupants',
            field=models.IntegerField(null=True),
        ),
    ]