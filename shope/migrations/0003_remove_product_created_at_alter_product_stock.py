# Generated by Django 5.1.3 on 2024-12-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0002_remove_category_description_category_category_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]
