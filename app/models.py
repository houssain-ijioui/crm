from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)


    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default=None)
    date_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.customer} ordered {self.product}'

    def serialize(self):
        return {
            "id": self.id,
            "customer": self.customer.name,
            "status": self.status,
            "product": self.product.name,
            "date_ordered": self.date_ordered
        }