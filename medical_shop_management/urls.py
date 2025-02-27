"""
URL configuration for the medical_shop_management project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from inventory.views import home, medicines_list, stocks_list, sales_list, inventory_list

urlpatterns = [
    path('', home, name='home'),  # Home URL
    path('admin/', admin.site.urls),  # Admin panel URL
    path('medicine/', medicines_list, name='medicine_list'),  # List of medicines
    path('stock/', stocks_list, name='stock_list'),  # List of stocks
    path('sell/', sales_list, name='sales_list'),  # List of sales
    path('inventory/', inventory_list, name='inventory_list'),  # Inventory overview
]
