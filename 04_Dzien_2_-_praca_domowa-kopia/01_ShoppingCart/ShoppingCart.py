from uuid import uuid4

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = uuid4()

class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        product_id = product.id
        if product_id in self.products:
            self.quantities[product_id] += 1
        else:
            self.products[product_id] = product
            self.quantities[product_id] = 1

    def remove_product(self, product):
        product_id = product.id
        if product_id in self.products:
            del self.products[product_id]
            del self.quantities[product_id]

    def change_product(self, product, new_quantity):
        product_id = product.id
        if product_id in self.products:
            if new_quantity == 0:
                del self.products[product_id]
                del self.quantities[product_id]
            elif new_quantity < 0:
                raise ValueError(f"Koszyk nie może być pusty.")
            else:
                 self.quantities[product_id] = new_quantity














bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)