# Generated by Django 2.2.7 on 2019-12-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_data',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
