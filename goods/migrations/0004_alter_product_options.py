# Generated by Django 5.0.6 on 2024-07-10 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]