from django.urls import path
from . views import DeliveryPostView, DeliveryGetView, DeliveryPutView
urlpatterns = [
    path('delivery/create/', DeliveryPostView.as_view()), # Haydovchi elon qo'shish
    path('delivery/detail/', DeliveryGetView.as_view()), # Haydovchi elon qo'shish
    path('delivery/update/', DeliveryPutView.as_view()), # Haydovchi elon qo'shish

]
