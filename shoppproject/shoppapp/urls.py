from django.contrib import admin
from django.urls import path,include
from . import views
app_name='shoppapp'
urlpatterns = [

    path('', views.allpdtcat,name='allpdtcat'),
    path('<slug:c_slug>/', views.allpdtcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.pdtdetails, name='prodcatdetails')
]
