from django.urls import path
from .import views
urlpatterns=[path('payment',views.merchent_for_pay),
             path('payment/status',views.merchent_check_payment),
             ]