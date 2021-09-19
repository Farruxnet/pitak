from django.urls import path
from . views import DriverApiView, DriverPutApiView, DriverGetApiView, \
 DriverCartPostApiView, DriverCartPutApiView, DriverCartGetApiView, DriverRatingPost, DriverRatingGet
urlpatterns = [
    path('driver/create/', DriverApiView.as_view()), # Haydovchi elon qo'shish
    path('driver/detail/', DriverGetApiView.as_view()), # Haydovchi elonini to'liq ko'rish
    path('driver/add-rating/', DriverRatingPost.as_view()), #
    path('driver/list-rating/', DriverRatingGet.as_view()), #
    path('driver/update/', DriverPutApiView.as_view()), # Haydovchi e'llonini o'zgartirish
    path('driver-cart/create/', DriverCartPostApiView.as_view()),
    path('driver-cart/detail/', DriverCartGetApiView.as_view()),
    path('driver-cart/update/', DriverCartPutApiView.as_view()),
]
