# Generated by Django 2.2.1 on 2020-02-17 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='主键')),
                ('author_name', models.CharField(max_length=32, verbose_name='作者姓名')),
                ('gender', models.CharField(max_length=32, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
            ],
            options={
                'db_table': 'author',
                'verbose_name_plural': '作者表',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名字')),
                ('address', models.CharField(max_length=32, verbose_name='出版社地址')),
            ],
            options={
                'db_table': 'publish',
                'verbose_name_plural': 'publish',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学科的名字')),
                ('start_time', models.DateField(verbose_name='开始时间')),
            ],
            options={
                'db_table': 'subject',
                'verbose_name': '学科',
                'verbose_name_plural': '学科',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('type_name', models.CharField(max_length=32, verbose_name='类型名字')),
                ('description', models.TextField(verbose_name='描述')),
            ],
            options={
                'db_table': 'type',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32, verbose_name='用户名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('email', models.EmailField(default='11111@qq.com', max_length=254, verbose_name='电子邮箱')),
            ],
            options={
                'db_table': 'user',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish')),
            ],
            options={
                'db_table': 'book',
                'verbose_name_plural': 'book',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('date', models.DateField(verbose_name='时间日期')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('description', models.TextField(verbose_name='文章描述')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('tpye', models.ManyToManyField(to='app01.Type')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
