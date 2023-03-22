from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('product_list', views.product_list, name='product_list'),
    path('product_detail/<slug:product_detail_slug>/', views.product_detail, name='product_detail'),

    # url(r'^$', views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list,
    #     name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    #     views.product_detail,
    #     name='product_detail'),


]