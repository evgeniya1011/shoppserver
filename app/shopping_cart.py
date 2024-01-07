from typing import List, Optional
from models import Product


class ShoppingCart:
    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product):
        self.items.append(product)

    def add_items(self, products: List[Product]):
        self.items.extend(products)

    def remove_item(self, product: Product):
        if product in self.items:
            self.items.remove(product)

    def clear_cart(self):
        self.items = []

    def get_total_price(self) -> Optional[int]:
        if not self.items:
            return None
        return sum(product.price for product in self.items)
