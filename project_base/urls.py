from django.contrib import admin
from django.urls import path, include
from app_reg.views import regisztracio, pelda1, pelda2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regisztracio/', include('app_reg.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
