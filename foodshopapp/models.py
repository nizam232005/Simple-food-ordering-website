from django.db import models

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    GENDER_CHOICES=[
        ('F','Female'),
        ('M','Male'),
        ('O','Other'),
    ]
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    email=models.EmailField(max_length=1000,unique=True)
    password=models.CharField(max_length=100)
    image=models.FileField(upload_to='image/',null=True,blank=True)
    address=models.TextField(max_length=100)


class product(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    image=models.FileField(upload_to='image/',null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ('Coming Soon', 'Coming Soon'),
    ]
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,null=True,blank=True)


class cart(models.Model):
    user=models.ForeignKey(reg,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    totalprice=models.IntegerField(null=True,blank=True)



class favourite(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Ensure a user can only have one instance of a product in favourites
    

    