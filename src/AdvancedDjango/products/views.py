from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

def product_create_view(request):
    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    context = {}
    return render(request, "product/detail.html", context)
