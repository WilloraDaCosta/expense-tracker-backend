from django.contrib import admin
from django.urls import path, include
from expenses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('expenses.urls')),  # Add this line
    path('', views.home, name='home'),  # Add this line to route the root URL to the home view
]
