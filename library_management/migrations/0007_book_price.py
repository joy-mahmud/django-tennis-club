# Generated by Django 5.1.3 on 2024-12-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0006_alter_profile_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]