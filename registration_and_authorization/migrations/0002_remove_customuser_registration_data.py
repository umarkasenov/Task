# Generated by Django 5.0.2 on 2024-03-03 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_and_authorization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='registration_data',
        ),
    ]
