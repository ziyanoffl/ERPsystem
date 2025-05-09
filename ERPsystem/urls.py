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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from CRM.views import customer_management_view, customer_update, supplier_management_view, supplier_update
from ERPsystem.views import home_view, login_view, signup_view, custom_login, generate_openai_response, \
    ai_analysis_view, ai_chatbot_view, open_ai_chatbot
from Inventory.views import warehouse_management_view, warehouse_update, warehouse_delete, raw_material_view, \
    raw_material_update, raw_material_inventory_list, product_inventory_view
from Production.views import product_info_view, create_product, CreateProductionOrderView, production_order_list
from PurchaseOrder.views import create_purchase_order, purchase_order_list
from SalesOrder.views import add_sales_order, sales_order_view, update_order_status

urlpatterns = [
    path('', home_view, name='home_view'),
    path('admin/', admin.site.urls),
    path('login', login_view, name='login_view'),
    path('signup', signup_view, name='signup_view'),
    path('custom-login/', custom_login, name='custom_login'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout'),
    path('edit_password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='edit_password'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Purchase Order section #################################
    path('Purchase-Management/add-new', create_purchase_order, name='create_purchase_order'),
    path('Purchase-Management/view-orders', purchase_order_list, name='purchase_order_list'),

    # production section #####################################
    path('product', product_info_view, name='product_info_view'),
    path('add-product', create_product, name='create_product'),
    path('create_production_order/', CreateProductionOrderView.as_view(), name='create_production_order'),
    path('production-orders/', production_order_list, name='production_order_list'),

    # Inventory section ######################################
    path('warehouse', warehouse_management_view, name='warehouse_management_view'),
    path('warehouse/update/<int:pk>/', warehouse_update, name='warehouse_update'),
    path('warehouse/delete/<int:pk>/', warehouse_delete, name='warehouse_delete'),

    path('raw_material', raw_material_view, name='raw_material_view'),
    path('raw_material/update/<int:pk>/', raw_material_update, name='raw_material_update'),
    path('raw_material_inventory/', raw_material_inventory_list, name='raw_material_inventory_list'),

    path('product-inventory/', product_inventory_view, name='product_inventory'),

    # CRM ####################################################
    path('CRM/customers', customer_management_view, name='customer_management_view'),
    path('CRM/customers/update/<int:pk>/', customer_update, name='customer_update'),

    path('CRM/suppliers', supplier_management_view, name='supplier_management_view'),
    path('CRM/suppliers/update/<int:pk>/', supplier_update, name='supplier_update'),

    # path('CRM/suppliers', supplier_management_view, name='customer_management_view'),
    # path('CRM/suppliers/update/<int:pk>/', supplier_update, name='supplier_update'),

    # Sales Management #######################################
    path('add_sales_order/', add_sales_order, name='add_sales_order'),
    path('sales-orders/', sales_order_view, name='sales_order'),
    path('update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),
    # path('custom-signup/', custom_signup, name='custom_signup'),

    # AI
    path('ai_analysis/', ai_analysis_view, name='ai_analysis_view'),
    path('ai_chatbot/', ai_chatbot_view, name='ai_chatbot_view'),
    path('open_ai_chatbot/', open_ai_chatbot, name='open_ai_chatbot'),
    path('generate_openai_response/', generate_openai_response, name='generate_openai_response'),
]
