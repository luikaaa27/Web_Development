from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from api.models import Product,Category
from django.http import Http404

def index(request):
    latest_product_list = Product.objects.order_by('id')[:5]
    template = loader.get_template('api/index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))

def getProduct(request,pk):
    product = Product.objects.get(id = pk)
    template = loader.get_template('api/product.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(request, context))

def categories(request):
    latest_category_list = Category.objects.order_by('id')
    template = loader.get_template('api/categories.html')
    context = {
        'latest_category_list': latest_category_list,
    }
    return HttpResponse(template.render(context, request))

def getCategory(request,pk):
    category = get_object_or_404(Category, id = pk)
    return render(request, 'api/category.html',{'category': category})
