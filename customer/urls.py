from django.urls import path
from . views import CustomerPostView, CustomerPutView, CustomerGetView

urlpatterns = [
    path('customer/create/', CustomerPostView.as_view()), # Haydovchi elon qo'shish
    path('customer/update/', CustomerPutView.as_view()), # Haydovchi elon qo'shish
    path('customer/detail/', CustomerGetView.as_view()), # Haydovchi elon qo'shish
]
