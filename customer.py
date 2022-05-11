from shoppingcart import ShoppingCart
class Customer:
    def __init__(self, name):
        self.cust_name = name
        self.cust_shopping_cart = ShoppingCart()

    def add_to_cust_cart(self):
        self.cust_shopping_cart.add_to_cart()

    def view_cust_cart(self):
        for item in self.cust_shopping_cart.shopping_cart:
            print(item.product_name)


