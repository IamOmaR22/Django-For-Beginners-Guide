from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView
from apps.common.views import HomeView, SignUpView, DashboardView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generator/', include('generator.urls')),
    #path('', TemplateView.as_view(template_name='example.html')),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

