# Generated by Django 5.1.3 on 2024-11-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(default=30, max_length=10),
            preserve_default=False,
        ),
    ]
