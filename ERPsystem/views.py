from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_view')
def home_view(request):
    # Check for the custom context variable indicating a successful login
    login_success = request.session.pop('login_success', False)
    # Print a message to the console
    print(f'login_success value: {login_success}')
    return render(request, 'dashboard.html', {'login_success': login_success})


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
