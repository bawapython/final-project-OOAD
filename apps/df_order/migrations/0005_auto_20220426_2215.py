# Generated by Django 2.0.7 on 2022-04-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0004_auto_20220425_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='oaddress',
            field=models.CharField(default='', max_length=150, verbose_name='order_address'),
        ),
    ]
