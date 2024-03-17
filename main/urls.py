
from django.urls import path

from .views import index,save_data,Login,WebPhish_login

urlpatterns = [
    path('', index,name="index"),
    path('save_data',save_data,name="save_data"),
    # path('login',Login.as_view(),name="login"),
    path('login',WebPhish_login,name="login"),
]
