# Generated by Django 3.1.2 on 2020-10-01 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]