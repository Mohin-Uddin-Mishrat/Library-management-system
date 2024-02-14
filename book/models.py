from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField( max_length = 15 )
    category = models.CharField(max_length =12, null =True, blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='midia/uploads/')
    borrowing_price = models.DecimalField(max_digits = 12 , decimal_places=2)

    def __str__(self):
        return self.title
    


class reviews(models.Model):
    user = models.ForeignKey(User, related_name = 'review', on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name = 'review' , on_delete = models.CASCADE )
    comment = models.TextField()

class BorrowReportModel(models.Model):
    user =       models.ForeignKey(User , related_name = 'borrow' , on_delete = models.CASCADE)
    book =       models.ForeignKey(Book , related_name = 'borrow' , on_delete = models.CASCADE)
    price =      models.DecimalField(max_digits = 12, decimal_places =2)
    borrow =      models.BooleanField(default = False)
    handover =     models.BooleanField(default = False)
    balance_after_borrow = models.DecimalField(max_digits =12 , decimal_places =2)
    borrow_date =models.DateTimeField(auto_now_add = True) 
    return_date =models.DateTimeField(blank =True , null = True)

    
