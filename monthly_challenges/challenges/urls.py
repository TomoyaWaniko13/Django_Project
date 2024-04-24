from django.urls import path

from . import views

urlpatterns = [
    path("<int:int_month>", views.monthly_challenge_by_number),
    path("<str:str_month>", views.monthly_challenge, name="month-challenge")
]
