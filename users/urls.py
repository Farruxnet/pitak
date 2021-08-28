from django.urls import path
from . views import Register, UserProfile

urlpatterns = [
    path('user/register/', Register.as_view()),
    path('user/profile/', UserProfile.as_view()),
]
