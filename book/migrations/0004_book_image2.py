# Generated by Django 4.2.10 on 2024-02-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image2',
            field=models.URLField(blank=True, null=True, verbose_name='Укажите ссылку на фото'),
        ),
    ]
