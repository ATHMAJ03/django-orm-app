# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![Entity Diagram](entity.png)

## DESIGN STEPS

### STEP 1:
An Django application is created inside dataproject folder.

### STEP 2:
A python program is written to create a table to store and retrieve data.

### STEP 3:
The table is created with 6 fields in which the username field is made as PrimaryKey.

### STEP 4:
Then the project files migrated. A superuser is also created.

### STEP 5:
Now the server side program is executed .

### STEP 6:
The admin page of our website is accessed using username and password.

### STEP 7:
Records are added and saved in the table inside the database.



## PROGRAM

```
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

```

## OUTPUT

![Django-data-base](django-output.png)


## RESULT
Thus a Django application is successfully developed to store and retrieve data from a database using Object Relational Mapping(ORM).