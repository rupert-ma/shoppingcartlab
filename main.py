from product import Product
from shoppingcart import ShoppingCart
from customer import Customer

cust_one = Customer('Mike')
print(cust_one.cust_name)
cust_one.add_to_cust_cart()
cust_one.add_to_cust_cart()
cust_one.add_to_cust_cart()
cust_one.view_cust_cart()
cust_one.cust_shopping_cart.return_list()
cust_one.cust_shopping_cart.empty_cart()
cust_one.cust_shopping_cart.return_list()





