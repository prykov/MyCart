"""mycart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from userManagementApp.views import *
from adminApp.views import *
from cartApp.views import *

urlpatterns = [
    url(r'^base_admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^cart/(?P<cart_id>\d+)$', main),
    url(r'^product/delete/(\d+)$', user_product_delete),
    url(r'^product/create/(\d+)$', user_product_create),
    url(r'^product/create/$', main),
    url(r'^cart/create/$', user_cart_create),
]

# User
urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration),
]

# Admin
urlpatterns += [
    url(r'^admin/$', admin_page),
    url(r'^admin/user/update/(\d*)$', admin_user_update),
    url(r'^admin/user/delete/(\d+)$', delete_user),
    #url(r'^admin/get_user_form/(\d+)$', get_user_form),
    #url(r'^admin/create/user/(\d*)$', create_user),
    url(r'^admin/category/$', category_list),
    url(r'^admin/category/detail/(\d+)$', category_detail),
    url(r'^admin/category/update/(\d*)$', category_update),
    url(r'^admin/category/delete/(\d+)$', category_delete),
    url(r'^admin/cart/$', cart_list),
    url(r'^admin/cart/detail/(\d+)$', cart_detail),
    url(r'^admin/cart/update/(\d*)$', cart_update),
    url(r'^admin/cart/delete/(\d+)$', cart_delete),
    url(r'^admin/product/$', product_list),
    url(r'^admin/product/detail/(\d+)$', product_detail),
    url(r'^admin/product/update/(\d+)$', product_update),
    url(r'^admin/product/delete/(\d+)$', product_delete),
]
