# Generated by Django 2.2.1 on 2020-02-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0002_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(default=1, verbose_name='商品状态'),
        ),
    ]
