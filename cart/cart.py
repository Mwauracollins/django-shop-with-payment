from django.conf import settings
from decimal import Decimal
from products.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.add_cart_session()
        self.product_ids = self.get_product_ids()

        # Add a new session if there is none
    def add_cart_session(self):
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        return cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product in self.cart:
            del self.cart[product_id]
            self.save()

    # Total quantity of items in the cart
    def __len__(self):
        quantity = sum(item['quantity'] for item in self.cart.values())
        return quantity

    def get_product_ids(self):
        return [product_id for product_id in self.cart.keys()]

    def get_total_distinct_item(self):
        return len(self.product_ids)

    def get_total_price(self):
        return sum(Decimal(item['total_price']) for item in self.cart.items())

    def __iter__(self):
        product_ids = self.product_ids
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

