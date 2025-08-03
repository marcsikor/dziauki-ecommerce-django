from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/<int:id>', views.details, name = 'details'),
    path('new', views.new_posting, name = 'new_posting')
]