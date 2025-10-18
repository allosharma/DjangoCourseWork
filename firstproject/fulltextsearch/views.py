from django.shortcuts import render
from django.db.models import Subquery, OuterRef
from fulltextsearch.models import Product

# Create your views here.

def fulltextsearchindex(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    
    return render(request, 'ftsindex.html', context=context)

# def fulltextsearch(request):
#     if request.GET.get('query'):
#         query = request.GET.get('query')
#         products = Product.objects.filter(title__icontains=query)
#         context = {
#             'products': products
#         }
#         return render(request, 'ftsindex.html', context=context)