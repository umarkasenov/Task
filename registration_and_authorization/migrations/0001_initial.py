# Generated by Django 5.0.2 on 2024-03-03 15:12

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(60)])),
                ('phone_number', models.CharField(default='+996', max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('IT', 'Другое')], max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('status', models.CharField(choices=[('В сети', 'В сети'), ('Занят', 'Занят'), ('На работе', 'На работе'), ('В школе', 'В школе')], max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('social_media', models.URLField(blank=True)),
                ('interests', models.CharField(blank=True, max_length=100)),
                ('registration_data', models.DateTimeField(auto_now_add=True)),
                ('hobbies', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
