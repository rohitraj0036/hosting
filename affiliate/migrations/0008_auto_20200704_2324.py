# Generated by Django 3.0.6 on 2020-07-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0007_auto_20200704_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=600, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('categories', models.CharField(default='', max_length=60)),
                ('SubCategories', models.CharField(default='', max_length=60)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='image/mobile')),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.AddField(
            model_name='realme',
            name='description',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='realme',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='realme',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='xaiomi',
            name='description',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='xaiomi',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='xaiomi',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
