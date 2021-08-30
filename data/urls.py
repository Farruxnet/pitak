from django.urls import path
from . views import ProvinceApiView, DistrictApiView, AutomobileApiView, DerictionApiView, DistrictApiAllView

urlpatterns = [
    path('province/list/', ProvinceApiView.as_view()),
    path('district/list/<int:pk>', DistrictApiView.as_view()),
    path('district/list/', DistrictApiAllView.as_view()),
    path('deriction/list/', DerictionApiView.as_view()),
    path('automobile/list/', AutomobileApiView.as_view()),
]
