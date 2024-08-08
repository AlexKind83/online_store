from decimal import Decimal
from django.conf import settings
from online_store.store.models import Product


class Cart:
    """Добавляет данные в корзину либо хранит корзину пустой."""
    def __init__(self, request):
        # инициализация корзины
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Прокрутить товарные позиций корзины в цикле и получить товары из БД"""
        product_ibs = self.cart.keys()
        # получаем объекты product и добавляем в корзину
        products = Product.objects.filter(id_in=product_ibs)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Подсчитывает все товары в корзине."""
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """ Добавляет товар в корзину либо обновляет его количество."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Поместить сеанс как измененный, чтобы обеспечить его сохранение."""
        self.session.modified = True

    def get_total_price(self):
        """Подсчитывает общею стоимость всех товаров корзины"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def remove(self, product):
        """Удаление товара из корзины."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Очистка сеанса корзины"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
