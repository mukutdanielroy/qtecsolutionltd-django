from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Warranty(models.Model):
    duration = models.IntegerField()

    def __str__(self):
        if self.duration == 0:
            return "No warranty"
        return f"{self.duration} Year(s)"

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='product_image')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)

    def __str__(self):
        return self.title