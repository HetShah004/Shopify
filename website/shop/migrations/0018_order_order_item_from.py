# Generated by Django 3.2 on 2021-04-25 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_item_from',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
