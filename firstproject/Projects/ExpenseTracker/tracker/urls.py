from django.urls import path
from tracker.views import index, delete_transaction
urlpatterns = [
    path('', index, name='index'),
    path('delete-transaction/<uuid>/', delete_transaction, name='delete_transaction'),
]