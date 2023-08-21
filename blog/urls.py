
from django.contrib import admin
from django.urls import path, include
from .views import homepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepageView, name='homepage'),
]
