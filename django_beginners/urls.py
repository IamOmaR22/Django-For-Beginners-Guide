from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView
from apps.common.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generator', include('generator.urls')),
    #path('', TemplateView.as_view(template_name='example.html')),
    path('', SignUpView.as_view(), name='home')
]

