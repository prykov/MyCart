from django.shortcuts import render, get_object_or_404
from cartApp.forms import *
from django.shortcuts import HttpResponseRedirect


def main(request, cart_id=0):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user.id)
        product_form = UserProductForm()
        cart_form = UserCartForm()
        if cart_id:
            # Преобразую объект QS в список
            products = list(Product.objects.filter(cart=cart_id).values())
            # Добавляю поле n для получения порядкового номера в списке
            # и поле category для хранения имени категории
            for i in range(0, len(products)):
                products[i]['n'] = i + 1
                products[i]['category'] = Category.objects.get(id=products[i]['category_id']).name
            return render(request, 'index_test.html', {'carts': carts, 'products': products,
                                                       'product_form': product_form, 'cart_form': cart_form,
                                                       "cart_id": cart_id})
        else:
            try:
                products = list(Product.objects.filter(cart=carts[0].id).values())
                for i in range(0, len(products)):
                    products[i]['n'] = i + 1
                    products[i]['category'] = Category.objects.get(id=products[i]['category_id']).name
                return render(request, 'index_test.html', {'carts': carts, 'products': products,
                                                           'product_form': product_form, 'cart_form': cart_form,
                                                           "cart_id": carts[0].id})
            except:
                error = 'Сначала добавьте корзину'
                return render(request, 'index_test.html', {'product_form': product_form, 'cart_form': cart_form,
                                                           'error': error})
    else:
        return render(request, 'index.html')


# Удаление продукта из карзины
def user_product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    n = product.cart.id
    product.delete()
    return HttpResponseRedirect('/cart/' + str(n))


# Редактирование продукта пользователем
def user_product_update(requst, product_id):
    pass


# Добавление продукта в корзину пользователем
def user_product_create(request, cart_id):
    if request.method == 'POST':
        product = Product(cart=Cart.objects.get(id=cart_id))
        form = UserProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cart/' + cart_id)
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


# Добавление корзины пользователем
def user_cart_create(request):
    if request.method == 'POST':
        cart = Cart(user=request.user)
        form = UserCartForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
