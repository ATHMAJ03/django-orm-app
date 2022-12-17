from django.db import models
from django.contrib import admin

class Database(models.Model):
    customer_name = models.CharField(max_length=20)
    purchase_id= models.IntegerField(unique=True,primary_key=True)
    amount_of_product_purchased = models.IntegerField()
    contact_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50,unique=True)

class Admin(admin.ModelAdmin):
    list_display = ('customer_name', 'purchase_id', 'amount_of_product_purchased', 'contact_no','email')