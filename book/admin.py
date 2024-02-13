from django.contrib import admin
from .models import Book, reviews , BorrowReportModel
# Register your models here.
admin.site.register(Book)
admin.site.register(reviews)
admin.site.register(BorrowReportModel)