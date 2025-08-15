from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/<int:id>', views.details, name = 'details'),
    path('new', views.new_posting, name = 'new_posting'),
    path('edit/<int:id>', views.edit_posting, name = 'edit_posting'),
    # path('login', views.login, name = 'login'),
    # path('signup', views.signup, name = 'signup'),
    path("",include("django.contrib.auth.urls"))
]