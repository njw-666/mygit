# Generated by Django 2.2.1 on 2020-02-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_auto_20200226_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_picture',
            field=models.ImageField(default='img/1.jpg', upload_to='img', verbose_name='商品的图片'),
        ),
    ]
