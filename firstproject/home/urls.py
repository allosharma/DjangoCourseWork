from django.urls import path
from home.views import index, contact, dynamic_route, about, thank_you, htmlform, search_page

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('dynamic/<int:number>/', dynamic_route, name='dynamic_route'),
    path('about/', about, name='about'),
    path('thank_you/', thank_you, name='thank_you'),
    path('HTMLForm/', htmlform, name='HTMLForm'),
    path('search_page/', search_page, name='search_page'),
]