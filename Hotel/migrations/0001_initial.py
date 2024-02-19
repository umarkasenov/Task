# Generated by Django 4.2.10 on 2024-02-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('image', models.URLField(verbose_name='Укажите ссылку на фото')),
                ('rating', models.CharField(choices=[('1', '1 звезд'), ('2', '2 звезд'), ('3', '3 звезд'), ('4', '4 звезд'), ('5', '5 звезд')], max_length=100)),
                ('address', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField(blank=True)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.CharField(choices=[('15', '10%'), ('25', '25%'), ('35', '35%'), ('45', '45%'), ('55', '55%')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]