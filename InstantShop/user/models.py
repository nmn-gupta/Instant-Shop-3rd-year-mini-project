from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

def user_directory(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.username,filename)

class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    dob = models.DateField()
    phone_number = models.TextField(max_length=13)
    photo = models.ImageField(upload_to = user_directory, default='default-user-image.png')
    is_email_verified = models.BooleanField(default=False) 
    token = models.CharField(max_length = 30, primary_key = True)

    def __str__(self):
        return str(self.user.username)

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2) 
    product_uploaded_on_date = models.DateField()
    selled = models.BooleanField(default=False)
    features = models.TextField()
    months_of_product_used = models.IntegerField()

    img1 = models.ImageField(upload_to = user_directory ,blank=True)
    img2 = models.ImageField(upload_to = user_directory ,blank=True)
    img3 = models.ImageField(upload_to = user_directory ,blank=True)
    img4 = models.ImageField(upload_to = user_directory ,blank=True)

    def __str__(self):
        return self.name+" "+self.user.username


class Comment(models.Model):
    comment_done_by = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    date_of_comment = models.DateField(default=datetime.datetime.today)
    comment = models.TextField()

    def __str__(self):
        return str(self.id)


class ProductComments(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user_carted = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    product_carted = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_carted.user.username +" carted "+self.product_carted.name