from django.urls import path
from django.contrib import admin
from telecom import views
urlpatterns=[
    path('',views.admission_client),
    path('predict/',views.predict),
]
