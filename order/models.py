from django.db import models
from authentication.models import Customer

# Create your models here.


class Order(models.Model):
    """
    Order Table
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    item = models.CharField(max_length=200)
    amount = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item}_{self.amount}"
