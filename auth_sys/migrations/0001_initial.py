# Generated by Django 5.2.1 on 2025-06-22 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='auth_sys/')),
                ('description', models.TextField(blank=True, null=True)),
                ('birthday_day', models.DateField(blank=True, null=True)),
                ('permission', models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор')], default='user', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
