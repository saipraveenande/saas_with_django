from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm
app_name = 'core'

urlpatterns = [   
    path("", views.index, name = 'index'),
    path("dashboard/", views.dashboard, name='dashboard'),    
    path("donate/", views.Donatepage, name='donate'),    
    path('signup/', views.Signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
