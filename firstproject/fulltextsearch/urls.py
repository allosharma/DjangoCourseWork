from django.urls import path
from fulltextsearch.views import fulltextsearchindex

urlpatterns = [
    path('index/', fulltextsearchindex, name='ftshome'),
]