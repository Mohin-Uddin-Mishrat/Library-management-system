from django.shortcuts import render
from django.views.generic import FormView 
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView, LoginView
from .forms import registerForm 
from django.urls import reverse_lazy
from .models import Account
from decimal import Decimal
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = registerForm
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    
class userLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class userloginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class depositAmount(View):
    def get(self, request):
        return render(request, 'deposit.html')

    def post(self, request):
        input_value = request.POST.get('amount')
        user_balance = request.user.account.Balance
        user_acc = request.user.account
        
        user_balance += Decimal(input_value)
        
        user_acc.Balance = user_balance
        user_acc.save(
            update_fields =['Balance']
        )
        subject = "Deposit money alert"
        message = f"Dear {request.user.username}, you have successfully recieved {input_value} $, now your account Balance is {user_acc.Balance} $ "
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email]
        send_mail(subject, message, email_form, recipient_list)
        messages.success(request,f'Deposited Successfuly , Know more information , check your email account')
        return render(request, 'deposit.html')





























