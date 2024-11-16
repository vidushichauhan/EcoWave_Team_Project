from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from Auth.models import User


class Product(models.Model):
    # Existing fields
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry = models.IntegerField(default=3)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='products/')
    in_stock = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=10, default="1")
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(default=False, help_text="Mark this product as verified to display on homepage")
    # Trade-In Specific Fields
    condition_choices = [
        ('new', 'New'),
        ('like_new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('needs_repair', 'Needs Repair'),
    ]
    condition = models.CharField(
        max_length=20,
        choices=condition_choices,
        default='good',
        help_text='Condition of the product being traded in'
    )
    reason_for_trade_in = models.TextField(
        null=True,
        blank=True,
        help_text='Reason for trading in the product'
    )
    eco_friendly_certification = models.FileField(
        upload_to='certifications/',
        null=True,
        blank=True,
        help_text='Upload eco-friendly certification if applicable'
    )
    trade_in_preference_choices = [
        ('recycle', 'Recycle'),
        ('resell', 'Resell'),
        ('donate', 'Donate'),
    ]
    trade_in_preference = models.CharField(
        max_length=20,
        choices=trade_in_preference_choices,
        default='recycle',
        help_text='User preference for trade-in (recycle, resell, or donate)'
    )
    estimated_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Estimated trade-in value'
    )

    def __str__(self):
        return self.name

    def expire_date(self):
        return self.created_at + timedelta(days=self.expiry)

    def days_left(self):
        now = timezone.now()
        expire_date = self.expire_date()
        delta = expire_date - now
        return delta.days + 1


class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

@receiver(post_save, sender=Product)
def set_expiry_date(sender, instance, created, **kwargs):
    if created:
        instance.expiry_date = instance.created_at + timedelta(days=instance.expiry)
        instance.save()
    else:
        Product.objects.filter(id=instance.id).update(
            expiry_date=instance.created_at + timedelta(days=instance.expiry)
        )