from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
    path('product_detail/<slug:product_detail_slug>/', views.product_detail, name='product_detail'),
    re_path(r'cart/', views.cart, name='cart'),
    re_path(r'wishlist/', views.wishlist, name='wishlist'),


    # url(r'^$', views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list,
    #     name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #     views.product_detail,
    #     name='product_detail'),


]
