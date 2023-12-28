from django.urls import path
from .views import table_list, TableListCreateView

urlpatterns = [
    path('list/', table_list, name='table_list'),
    path('', TableListCreateView.as_view(), name='table-list-create'),   
]