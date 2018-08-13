from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    context = {}
    return render(request, "product/detail.html", context)
