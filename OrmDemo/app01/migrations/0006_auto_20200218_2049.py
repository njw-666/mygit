# Generated by Django 2.2.1 on 2020-02-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200218_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type_name',
            new_name='name',
        ),
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
    ]
