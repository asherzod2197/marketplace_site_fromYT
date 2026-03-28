from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='product_images/')
    

class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment of " + str(self.author.username)
    












