from django.contrib import admin
from django.urls import path

from relation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.insert),
    path('find/', views.find),
    path('find1/', views.find1),
]
