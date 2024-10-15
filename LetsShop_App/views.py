from django.shortcuts import render
from .models import * 
from .forms import *
from django.db.models import Q
from .models import Product


def home(request):
    slides = Slider.objects.all()
    
    return render(request,'home.html', {'slides': slides})




# def product_search_view(request):
#     form = ProductSearchForm(request.GET)
#     products = Product.objects.all()

#     if form.is_valid():
#         query = form.cleaned_data.get('query')
#         category = form.cleaned_data.get('category')
#         sub_category = form.cleaned_data.get('sub_category')
#         color = form.cleaned_data.get('color')
#         size = form.cleaned_data.get('size')
#         condition = form.cleaned_data.get('condition')

#         if query :
#             product = products.objects.filter(Q(title__icontains=query))
#         if category :
#             product = products.filter(Q(category=category))
#         if sub_category :
#             product = products.filter(Q(sub_category=sub_category))
#         if color :
#             product = products.filter(Q(color=color))
#         if size :
#             product = products.filter(Q(size=size))
#         if condition :
#             product = products.filter(Q(condition=condition))
#     context ={
#         'form':form,
#         'prod': products
#     }
#     return render(request, 'Product/search.html',context)
