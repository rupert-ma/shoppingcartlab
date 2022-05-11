from product import Product

class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
        
    def return_list(self):
        total_items_in_cart = len(self.shopping_cart)
        print(f'There are {total_items_in_cart} items in the shopping cart')
    
    def add_to_cart(self):
        product_name = input('What is the name of the product? ')
        product_price = input('What is the price of the product? ')
        product_category = input('What is the category of the product? ')
        new_product = Product(product_name, product_price, product_category)
        self.shopping_cart.append(new_product)

    def empty_cart(self):
        self.shopping_cart = []

        