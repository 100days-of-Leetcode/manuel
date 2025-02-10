class Product:
    def __init__(self, product_Id, product_Name, base_Price):
    self.product_Id = product_Id
    self.product_Name = product_Name
    self.base_Price = base_Price

    def apply_discount(self, percentage):
    discount_amount = (percentage / 100) * self.base_Price
    self.base_Price -= discount_amount

    def calculate_final_price(self):
    return self.base_Price

class Electronics(Product):
    def __init__(self, product_Id, product_Name, base_Price,
    warranty_period):
    super().__init__(product_Id, product_Name, base_Price)
    self.warranty_period = warranty_period

    def calculate_final_price(self):
    warranty_based_price = self.base_Price + (self.base_Price * 0.05 *
    self.warranty_period / 12)
    return warranty_based_price

class Clothing(Product):
    def __init__(self, product_Id, product_Name, base_Price, size,
    fabric_charge):
    super().__init__(product_Id, product_Name, base_Price)
    self.size = size
    self.fabric_charge = fabric_charge

    def calculate_final_price(self):
    return self.base_Price + self.fabric_charge

class Cart:
    def __init__(self):
    self.products = []
    def add_product(self, product):
    self.products.append(product)

    def calculate_total_price(self):
    total_price = sum(product.calculate_final_price() for product in
    self.products)
    return total_price

laptop = Electronics("E001", "Laptop", 1000.0, 24)
jacket = Clothing("C001", "Winter Jacket", 200.0, "M", 20.0)
laptop.apply_discount(10)
print(f"Final Price of Laptop: {laptop.calculate_final_price()}")
print(f"Final Price of Winter Jacket: {jacket.calculate_final_price()}")
cart = Cart()
cart.add_product(laptop)
cart.add_product(jacket)
print(f"Total Price of Products in Cart: {cart.calculate_total_price()}")
