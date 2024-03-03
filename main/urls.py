
from django.urls import path

from .views import index,save_data

urlpatterns = [
    path('', index,name="index"),
    path('save_data',save_data,name="save_data"),
]
