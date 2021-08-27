from django.urls import path
from . views import SmsView
urlpatterns = [
    path('sms-api/', SmsView.as_view()),
]
