# Generated by Django 4.2.10 on 2024-02-18 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image1',
        ),
    ]
