# Generated by Django 4.2.13 on 2024-07-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreenCartEcom', '0004_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
