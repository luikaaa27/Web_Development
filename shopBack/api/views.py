from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from api.models import Product,Category
from django.http import Http404, JsonResponse

'''def index(request):
    latest_product_list = Product.objects.order_by('id')[:5]
    template = loader.get_template('api/index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))'''

def index(request):
    products = Product.objects.all()
    json_products = [product.to_json() for product in products]
    return JsonResponse(json_products, safe=False)

'''def getProduct(request,pk):
    product = Product.objects.get(id = pk)
    template = loader.get_template('api/product.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(request, context))
'''
def getProduct(request,pk):
    try:
        product = Product.objects.get(id = pk)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(product.to_json())

'''def categories(request):
    latest_category_list = Category.objects.order_by('id')
    template = loader.get_template('api/categories.html')
    context = {
        'latest_category_list': latest_category_list,
    }
    return HttpResponse(template.render(context, request))
'''

def categories(request):
    categories = Category.objects.all()
    json_categories = [category.to_json() for category in categories]
    return JsonResponse(json_categories, safe=False)
    
'''
def getCategory(request,pk):
    category = get_object_or_404(Category, id = pk)
    return render(request, 'api/category.html',{'category': category})
'''
def getCategory(request,pk):
    try:
        category = Category.objects.get(id = pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(category.to_json())

def categoryProducts(request,pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    products = category.product_set.all()
    json_products = [product.to_json() for product in products]
    return JsonResponse(json_products, safe=False)
