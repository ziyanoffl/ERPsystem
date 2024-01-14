import openai
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from ERPsystem.settings import OPENAI_API_KEY
from Inventory.models import RawMaterial, Warehouse, ProductInventory, RawMaterialInventory
from Production.models import Product, ProductionOrder
from PurchaseOrder.models import PurchaseOrder
from SalesOrder.models import SalesOrder


@login_required(login_url='login_view')
def home_view(request):
    # Retrieve data for charts and table
    raw_materials = RawMaterial.objects.all()
    warehouses = Warehouse.objects.all()
    production_orders = ProductionOrder.objects.all()

    # Check for the custom context variable indicating a successful login
    login_success = request.session.pop('login_success', False)
    # Print a message to the console
    print(f'login_success value: {login_success}')

    # Data for Raw Material Inventory Chart
    raw_material_labels = [str(material) for material in RawMaterialInventory.objects.all()]
    raw_material_data = [inventory.quantity_on_hand for inventory in RawMaterialInventory.objects.all()]

    # Data for Product Inventory Chart
    product_labels = [str(product) for product in ProductInventory.objects.all()]
    product_data = [inventory.quantity_on_hand for inventory in ProductInventory.objects.all()]

    # Data for Production Orders Chart
    production_order_labels = [str(order.product) for order in ProductionOrder.objects.all()]
    production_order_data = [order.quantity for order in ProductionOrder.objects.all()]

    # Data for Purchase Orders Chart
    purchase_order_labels = [str(order.raw_material) for order in PurchaseOrder.objects.all()]
    purchase_order_data = [order.quantity for order in PurchaseOrder.objects.all()]

    return render(
        request,
        'dashboard.html',
        {
            'login_success': login_success,
            'raw_material_labels': raw_material_labels,
            'raw_material_data': raw_material_data,
            'product_labels': product_labels,
            'product_data': product_data,
            'production_order_labels': production_order_labels,
            'production_order_data': production_order_data,
            'purchase_order_labels': purchase_order_labels,
            'purchase_order_data': purchase_order_data,
        }
    )


def login_view(request):
    return render(request, 'accounts/login.html')


# def signup_view(request):
#     return render(request, 'accounts/signup.html')


def custom_login(request):
    if request.method == 'POST':
        # Get the username and password from the submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user if authentication is successful
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            # Set a custom context variable to indicate a successful login
            request.session['login_success'] = True
            # Print a message to the console
            print('User successfully logged in. Redirecting to home.')
            return redirect('home_view')  # Change 'home' to the desired redirect URL
        else:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid login credentials.')

    # Render the custom login template for GET requests
    return render(request, '')  # Replace 'your_app/login.html' with your actual template path


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered and logged in.')
            return redirect('home_view')  # Change 'home' to the desired redirect URL
        else:
            messages.error(request, 'Registration failed. Please correct the errors in the form.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


# Open AI key responses
def generate_openai_response(request):
    print("Function called")  # Check if the function is called
    if request.method == 'POST':
        try:
            # Extract data from the POST request
            table_type = request.POST.get('tableType')
            gpt_model = request.POST.get('gptModel')

            # Choose the appropriate model based on the table_type parameter
            if table_type == 'product':
                model_data = Product.objects.order_by('-product_id')[:10]
            elif table_type == 'recent_sales':
                model_data = SalesOrder.objects.order_by('-order_date')[:10]
            elif table_type == 'product_inventory':
                model_data = ProductInventory.objects.order_by('-id')[:10]
            elif table_type == 'recent_purchases':
                model_data = PurchaseOrder.objects.order_by('-order_id')[:10]
            elif table_type == 'raw_material_inventory':
                model_data = RawMaterialInventory.objects.order_by('-id')[:10]
            else:
                return JsonResponse({'error': 'Invalid table_type'})

            # Extract relevant data from the database
            table_name = model_data.model._meta.db_table  # Get the actual table name
            column_names = [field.name for field in model_data.model._meta.fields]

            # Build the CSV header
            rows_as_csv = [','.join([table_name] + column_names)]  # Add table name as a header

            # Build CSV rows
            for product in model_data:
                row_values = [str(getattr(product, field.name)) for field in product._meta.fields]
                rows_as_csv.append(','.join(row_values))

            # Add column names to the CSV data

            for product in model_data:
                # Assuming all fields in the model are relevant
                row_values = [str(getattr(product, field.name)) for field in product._meta.fields]
                rows_as_csv.append(','.join(row_values))

            openai.api_key = OPENAI_API_KEY

            # Create a prompt incorporating the database content
            prompt = f"Analyze the following data and provide brief insights: {', '.join(rows_as_csv)}"

            response = openai.chat.completions.create(
                messages=[
                    {"role": "system",
                     "content": "You are an intelligent AI integrated within an ERP system to provide insights and trends in data and be helpful. "
                                "I'll send you some database data, you should act your role and give short and very very brief insights or trends"},
                    {"role": "user", "content": prompt},
                ],
                model=gpt_model,
                # model="gpt-4-1106-preview",
            )

            response_message = response.choices[0].message.content
            print(prompt)

            return JsonResponse({'generated_response': response_message})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def open_ai_chatbot(request):
    if request.method == 'POST':
        try:
            # Extract data from the POST request
            table_type = request.POST.get('tableType')
            user_question = request.POST.get('userQuestion')
            gpt_model = request.POST.get('gptModel')

            # Choose the appropriate model based on the table_type parameter
            if table_type == 'product':
                model_data = Product.objects.order_by('-product_id')[:10]
            elif table_type == 'recent_sales':
                model_data = SalesOrder.objects.order_by('-order_date')[:10]
            elif table_type == 'product_inventory':
                model_data = ProductInventory.objects.order_by('-id')[:10]
            elif table_type == 'recent_purchases':
                model_data = PurchaseOrder.objects.order_by('-order_id')[:10]
            elif table_type == 'raw_material_inventory':
                model_data = RawMaterialInventory.objects.order_by('-id')[:10]
            else:
                return JsonResponse({'error': 'Invalid table_type'})

            # Extract relevant data from the database
            table_name = model_data.model._meta.db_table  # Get the actual table name
            column_names = [field.name for field in model_data.model._meta.fields]

            # Build the CSV header
            rows_as_csv = [','.join([table_name] + column_names)]  # Add table name as a header

            # Build CSV rows
            for product in model_data:
                row_values = [str(getattr(product, field.name)) for field in product._meta.fields]
                rows_as_csv.append(','.join(row_values))

            # Add column names to the CSV data
            for product in model_data:
                # Assuming all fields in the model are relevant
                row_values = [str(getattr(product, field.name)) for field in product._meta.fields]
                rows_as_csv.append(','.join(row_values))

            openai.api_key = OPENAI_API_KEY

            # Create a prompt incorporating the database content and user question
            prompt = f"This is the data: {', '.join(rows_as_csv)}\nUser Question: {user_question}"

            response = openai.chat.completions.create(
                messages=[
                    {"role": "system",
                     "content": "You are an intelligent AI integrated within an ERP system to provide insights and trends in data and to be helpful.\
                      I'll send you some database data and add a question about that data, give correct and brief answers to them.\
                       If the question is empty after User Question: ,list 5 suggested questions without answers."},
                    {"role": "user", "content": prompt},
                ],
                model=gpt_model,
                # model="gpt-4-1106-preview",
            )

            response_message = response.choices[0].message.content
            print(prompt)

            return JsonResponse({'generated_response': response_message})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'error': 'Invalid request method'})


def ai_analysis_view(request):
    return render(request, 'AI Analysis/analysis_page.html')


def ai_chatbot_view(request):
    return render(request, 'AI Analysis/ai_chatbot.html')
