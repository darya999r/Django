from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    registered_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'Username: {self.name}, emai: {self.email}, phone: {self.phone}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default='999999,99', max_digits=8, decimal_places=2)
    count = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'Заказ номер {self.pk} клиента {self.customer}'