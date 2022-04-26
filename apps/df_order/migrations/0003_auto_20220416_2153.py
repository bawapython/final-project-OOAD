# Generated by Django 2.0.7 on 2022-04-16 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0002_auto_20181218_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetailinfo',
            options={'verbose_name': 'order_details', 'verbose_name_plural': 'order_details'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': 'Orders', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='count',
            field=models.IntegerField(verbose_name='goods_count'),
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='products'),
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_order.OrderInfo', verbose_name='orders'),
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='goods_price'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='oIsPay',
            field=models.BooleanField(default=False, verbose_name='is_pay'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='oaddress',
            field=models.CharField(max_length=150, verbose_name='order_address'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='odate',
            field=models.DateTimeField(auto_now=True, verbose_name='order_time'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='oid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='order_no'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ototal',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='order_users'),
        ),
    ]
