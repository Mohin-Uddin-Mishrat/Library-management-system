
from django.urls import path
from .views import UserRegistrationView, userLogout, userloginView, depositAmount
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name ='register' ),
    path('logout/',userLogout.as_view(), name = 'logout' ),
    path('login/',userloginView.as_view(), name = 'login' ),
    path('deposit/',depositAmount.as_view(), name = 'deposit' ),
]
