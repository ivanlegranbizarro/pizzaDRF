from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
        ('D', 'Delivered'),
        ('C', 'Cancelled')
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    size = models.CharField(max_length=20, choices=SIZES, default='S')
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default='P')
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Customer: {self.customer.username} | {self.customer.phone_number} - Size: {self.size} - Quantity: {self.quantity} - Status: {self.order_status}'
