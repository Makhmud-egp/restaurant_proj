# Generated by Django 5.1.3 on 2024-12-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
