# Generated by Django 4.2.10 on 2024-02-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Book',
        ),
    ]