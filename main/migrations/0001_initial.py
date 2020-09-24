# Generated by Django 3.0.5 on 2020-08-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=10)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.CharField(max_length=100, null=True)),
                ('product_des', models.TextField(blank=True, max_length=1000)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
    ]
