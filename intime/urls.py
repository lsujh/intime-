from django.contrib import admin
from django.urls import path
from button_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add, name='add'),
]
