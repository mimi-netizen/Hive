from django.urls import path
from .views import login_view, RegisterView

urlpatterns = [
     path('login/', login_view, name='login'),
     path('register/', RegisterView.as_view(), name='register')
]
