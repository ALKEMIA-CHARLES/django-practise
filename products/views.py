# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():

#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj

    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_edit.html", context)

def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products':products
    }

    return render(request, "products/product_list.html", context)

def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items':items
    }
    return HttpResponseRedirect(reverse('product_list_view'))


# def delete_product(request, pk):
#     Product.objects.filter(id=pk).delete()
#     items = Product.objects.all()
#     context = {
#         'items': items
#     }
#     return redirect('product_list_view')
