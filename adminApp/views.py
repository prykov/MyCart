from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from userManagementApp.forms import *
from cartApp.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test


# Главная страница админки
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/')
    return render(request, 'admin_page.html', {'users': users, 'form': form})


# Редактирование пользователей
@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'admin_user_update.html', {'form': user})
    else:
        form = UserChangeForm(instance=user)
        return render(request, 'admin_user_update.html', {'user_name': user.username, 'user_id': user.id, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin/')


# Категории
@user_passes_test(lambda u: u.is_superuser)
def category_list(request):
    categories = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/category/')
        else:
            return HttpResponseRedirect('/admin/category/')
    else:
        return render(request, 'category_page.html', {'categories': categories, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category_detail.html', {"category": category})


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return HttpResponseRedirect('/admin/category/')


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/category/')
        else:
            return render(request, 'category_update.html', {'form': form})
    else:
        form = CategoryForm(instance=category)
        return render(request, 'category_update.html', {'form': form})


# Продукты
@user_passes_test(lambda u: u.is_superuser)
def product_list(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/product/')
        else:
            return render(request, 'product_update.html', {'form': form})
    else:
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return render(request, 'product_page.html', {'products': products, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {"product": product})


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/product/')
        else:
            return
    else:
        form = ProductForm(instance=product)
        return render(request, 'product_update.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def product_delete(requeset, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return HttpResponseRedirect('/admin/product')


# Корзина
@user_passes_test(lambda u: u.is_superuser)
def cart_list(request):
    carts = Cart.objects.all()
    form = CartForm()
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/cart/')
        else:
            return HttpResponseRedirect('/admin/cart/')
    else:
        return render(request, 'cart_page.html', {'carts': carts, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    products = Product.objects.filter(cart=cart_id)
    return render(request, 'cart_detail.html', {"cart": cart, 'products': products})


@user_passes_test(lambda u: u.is_superuser)
def cart_delete(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return HttpResponseRedirect('/admin/cart/')


@user_passes_test(lambda u: u.is_superuser)
def cart_update(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/cart/')
        else:
            return render(request, 'cart_update.html', {'form': form})
    else:
        form = CartForm(instance=cart)
        return render(request, 'cart_update.html', {'form': form})
