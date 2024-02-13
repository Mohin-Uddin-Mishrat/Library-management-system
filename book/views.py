from django.db.models.query import QuerySet
from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic import  ListView
from django.http import HttpResponse
from django.views import View
from .models import Book ,reviews , BorrowReportModel
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
class productView(View):
    def get(self , request ):
           book = Book.objects.all()
           return render(request , 'book.html', {'book':book})
    
    
             
    
class borrowView(View):
    def get(self , request, id):
        if request.user.is_authenticated :
               boi = Book.objects.get(id = id)
               if request.user.account.Balance >= boi.borrowing_price:
                    request.user.account.Balance -= boi.borrowing_price
                    request.user.account.save()
               
                    borrowCount = BorrowReportModel.objects.filter(user = request.user , book = boi , borrow = True ).count()
                    print(borrowCount)
                    if borrowCount == 0:
                         BorrowReportModel.objects.create(
                            user =   request.user,
                            book = boi,
                            price =  boi.borrowing_price  ,  
                            borrow =   True   ,
                            balance_after_borrow = request.user.account.Balance
                         )
                    else :
                         messages.success(self.request, "You have already borrowed this book")
                         return redirect('details',id = id)
                         
                    messages.success(self.request,"Successfully borrwed this book")
                    return redirect('details', id= id)
               else :
                     messages.error(self.request, f'Sorry you are Poor,  get rich bro , go to the deposit option then diposit money')
                     return redirect('details', id=id)
        else :
             return redirect('login')
    
class returnVIew(View):
    def get(self , request, id):
        if request.user.is_authenticated :
              boi = Book.objects.get(id = id)
              if BorrowReportModel.objects.filter(user = request.user , book =boi , borrow = True).exists():
                    request.user.account.Balance += boi.borrowing_price
                    request.user.account.save()
                    balance = request.user.account.Balance
               
                    borrowCount = BorrowReportModel.objects.filter(user = request.user , book = boi , borrow = True ).count()
                    if borrowCount == 1:
                         report = BorrowReportModel.objects.get(user = request.user , book = boi , borrow = True)
                         
                         report.borrow = False
                         report.balance_after_borrow = balance 
                         report.handover = True
                         report.return_date =timezone.now()
                         report.save()
                    else :
                         messages.success(self.request,"You have already returned this book")
                         return redirect('details', id =id)
                    messages.success(self.request,'Successfully returned this book')
                    return redirect('details', id= id)
              else :
                   messages.success(self.request,'first buy then return')
                   return redirect('details', id= id)
        else :
              return redirect('login')

             
      
    

class detailsView(View):
    def get(self , request , id):
           book = get_object_or_404(Book, id=id)
           review = reviews.objects.filter(book = book)
           is_borrowed = None
           if request.user.is_authenticated :
                is_borrowed = BorrowReportModel.objects.filter(user = request.user , book =book).exists()
           
           return render(request , 'details.html', {'book':book , 'reviews': review , 'boolean': is_borrowed })

    def post(self , request , id):
           book = get_object_or_404(Book, id=id)
           review = reviews.objects.filter(book = book)
           text = request.POST.get('reviewPost')
           isreviewExist = reviews.objects.filter(book=book, user = request.user).exists()
           print(isreviewExist)
           if text and  not isreviewExist :
                crate = reviews.objects.create(
                    book = book,
                    comment =  text,
                    user = request.user
                )
                return redirect('details', id = id)
           else :
                return redirect('details', id = id)

  

class profile(LoginRequiredMixin, ListView):
     template_name = 'profile.html'
     model = BorrowReportModel
     countBook = 0
     def get_queryset(self) :
          return super().get_queryset().filter(user = self.request.user)
     
     def get_context_data(self, **kwargs):
        self.countBook = BorrowReportModel.objects.filter(user = self.request.user).count()
        context = super().get_context_data(**kwargs)
        context['countBook'] = self.countBook
        return context

