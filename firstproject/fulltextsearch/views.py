from django.shortcuts import render
from django.db.models import Q
from fulltextsearch.models import Product
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity

def fulltextsearchindex(request):
    search = request.GET.get('search')

    if search:
        query = SearchQuery(search)
        vector = (
            SearchVector('title', weight='A')
            + SearchVector('description', weight='B')
            + SearchVector('category', weight='C')
            + SearchVector('brand', weight='D')
        )

        rank = SearchRank(vector, query)
        products = Product.objects.annotate(
            rank=rank,
            # When you are using TrigramSimilary, remember to use distinct() to avoid duplicate results
            # Also, you have to enable the use of the pg_trgm extension in your database
            # In PG Admin, you can go to the dataabase that you are using and inside queryt tool, you can enable the pg_trgm extension "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
            # To validate if it has been enabled properly you can run "SELECT * FROM pg_extension;" and see if pg_trgm is listed there
            similarity=(
                TrigramSimilarity('title', search)
                + TrigramSimilarity('description', search)
                + TrigramSimilarity('category', search)
                + TrigramSimilarity('brand', search)
            )
        ).filter(Q(rank__gt=0.1) | Q(similarity__gt=0.1)).distinct().order_by('-rank', '-similarity')

        for product in products:
            print(product.rank)
    else:
        products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'ftsindex.html', context=context)
