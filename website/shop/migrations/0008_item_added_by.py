# Generated by Django 3.2 on 2021-04-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_item_dec_item_item_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
