# Generated by Django 5.1.3 on 2024-11-28 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0004_remove_book_author_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
