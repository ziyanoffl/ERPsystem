from django.shortcuts import render, redirect
from ERPsystem.forms import ProductForm


# Create your views here.
def product_info_view(request):
    return render(request, 'production/product_information.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')  # Redirect to a success page or another view
    else:
        form = ProductForm()

    return render(request, 'production/add_product.html', {'form': form})
