from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views import generic
# Create your views here.
from .forms import ProductRegisterForm, LoadCategoriesForm
from .models import Product, Category
from .filters import ProductFilter
import csv
from io import StringIO

def index(request):
    return render(request, 'products/index.html')


def product_list(request):
    product_list = []
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    for product in filter.qs:
        category_set = Category.objects.filter(product=product.id)
        product_list.append((product, category_set))

    context = {
        'product_list':product_list,
        'filter':filter
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.delete()

        return redirect('product_list')
    else:
        product = Product.objects.get(id=product_id)
        template = loader.get_template('products/product_detail.html')
        context = {
            'product':product
        }
        return HttpResponse(template.render(context, request))

def product_register(request):
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get("description")
            value = form.cleaned_data.get("value")
            categories = Category.objects.filter(name__in=form.cleaned_data['category'])
            categories = form.cleaned_data['category']
            instance = Product.objects.create(
                                        name=name,
                                        description=description,
                                        value=value)
            instance.category.set(categories)
            instance.save()
            return redirect("index")

        else:
            return redirect('')
    else:
        form  = ProductRegisterForm()

        return render(request, 'products/product_register.html', {'form':form})

    return render(request, 'products/product_register.html')


def product_update(request, product_id):
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=product_id)
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get("description")
            product.value = form.cleaned_data.get("value")

            categories = Category.objects.filter(name__in=form.cleaned_data['category'])
            categories = form.cleaned_data['category']
            product.category.set(categories)
            product.save()
            return redirect("product_list")

        else:
            return redirect('index')
    else:
        product = Product.objects.get(id=product_id)

        form  = ProductRegisterForm(instance=product)#product)

        return render(request, 'products/product_update.html', {'form':form, "product_id":product_id})

    return render(request, 'products/product_update.html')


def category_load(request):
    if request.method == 'POST':
        form  = LoadCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['categories_csv'].read().decode('utf-8')
            csv_data = csv.reader(StringIO(file), delimiter=',')
            csv_data = list(csv_data)
            csv_data = [csv_data[i][0] for i in range(1, len(csv_data))]

            for category_name in csv_data:
                category = Category(name=category_name)
                category.save()
            return redirect("index")
        else:
            pass
    else:
        form  = LoadCategoriesForm()

        return render(request, 'products/category_load.html', {'form':form})

    return render(request, 'products/category_load.html')
