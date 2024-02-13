from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Account
class registerForm(UserCreationForm):

    class Meta :
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

     
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                    'class' : (
                    'appearance-none block w-full bg-slate-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-2 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 

            })


    def save(self, commit = True) :
             
        our_user = super().save(commit=False)

        if commit  :
            our_user.save()
            Account.objects.create(
               User = our_user 
            )
        return our_user


