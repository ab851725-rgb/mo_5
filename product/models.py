from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=155)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text