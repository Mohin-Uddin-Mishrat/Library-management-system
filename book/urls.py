
from django.urls import path 
from .views import productView ,detailsView, borrowView , returnVIew, profile
urlpatterns = [
    path('', productView.as_view(), name= 'products'),
    path('details/<int:id>', detailsView.as_view(), name= 'details'),
    path('review/<int:id>', detailsView.as_view(), name= 'reviewPost'),
    path('borrow/<int:id>', borrowView.as_view(), name= 'borrow'),
    path('return/<int:id>', returnVIew.as_view(), name= 'return'),
    path('profile', profile.as_view(), name= 'profile'),
]

