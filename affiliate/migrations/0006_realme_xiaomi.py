# Generated by Django 3.0.6 on 2020-07-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0005_auto_20200704_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='realme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categories', models.CharField(default='', max_length=60)),
                ('descirption', models.CharField(max_length=600)),
                ('prices', models.CharField(max_length=10)),
                ('SubCategories', models.CharField(default='', max_length=60)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/realme')),
            ],
        ),
        migrations.CreateModel(
            name='xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categories', models.CharField(default='', max_length=60)),
                ('descirption', models.CharField(max_length=600)),
                ('prices', models.CharField(max_length=10)),
                ('SubCategories', models.CharField(default='', max_length=60)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/xaiomi')),
            ],
        ),
    ]