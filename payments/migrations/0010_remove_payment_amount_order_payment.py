# Generated by Django 4.2.13 on 2024-07-16 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_order_remove_payment_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Amount',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='payments.payment'),
        ),
    ]
