# Generated by Django 4.2.13 on 2024-07-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_amount_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='stripe_payment_intent_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
