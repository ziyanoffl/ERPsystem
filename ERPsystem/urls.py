"""
URL configuration for ERPsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from ERPsystem.views import home_view, login_view, signup_view, custom_login
from Inventory.views import warehouse_management_view, warehouse_update, warehouse_delete, raw_material_view
from Production.views import product_info_view, create_product

urlpatterns = [
    path('', home_view, name='home_view'),
    path('admin/', admin.site.urls),
    path('login', login_view, name='login_view'),
    path('signup', signup_view, name='signup_view'),
    path('custom-login/', custom_login, name='custom_login'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout'),

    # production section
    path('product', product_info_view, name='product_info_view'),
    path('add-product', create_product, name='create_product'),

    # Inventory section
    path('warehouse', warehouse_management_view, name='warehouse_management_view'),
    path('warehouse/update/<int:pk>/', warehouse_update, name='warehouse_update'),
    path('warehouse/delete/<int:pk>/', warehouse_delete, name='warehouse_delete'),

    path('raw_material', raw_material_view, name='raw_material_view'),

    # path('custom-signup/', custom_signup, name='custom_signup'),
]
