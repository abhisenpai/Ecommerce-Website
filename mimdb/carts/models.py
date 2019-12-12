from django.db import models
from products.models import Product
# Create your models here.

class CartItem(models.Model):
    cart =models.ForeignKey('Cart',null=True,blank=True,on_delete='CASCADE')
    #cart foreign key
    product = models.ForeignKey(Product,on_delete='CASCADE')
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99,max_digits=64,decimal_places=2)
    #line_total
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)


    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem,null=True,blank=True)
    #products = models.ManyToManyField(Product,null=True,blank=True)
    total = models.DecimalField(max_digits=64,decimal_places=2,default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return "Cart id:"+str(self.id)