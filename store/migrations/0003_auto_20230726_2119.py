# Generated by Django 3.1 on 2023-07-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriprion',
            new_name='description',
        ),
    ]
