# Generated by Django 5.1.3 on 2024-11-28 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0005_rename_author_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='library_management.author'),
        ),
    ]
