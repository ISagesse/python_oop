# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

class Product:
    def __init__(self, price, item_name, weight, brand, status = 'for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        
    def sell(self):
        self.status = 'sold'
        return self
        
    def add_tax(self, tax):
        self.price += (self.price * tax)
        return self
    
    def return_item(self, reason):
        if reason == 'defective':
            self.price = 0
            self.status = 'defective'
            
        if reason == 'return':
            result = self.price * 0.20
            self.price -= result
            self.status = 'used'
            
        return self
            
    def display_info(self):
        print(
            f' Name: {self.item_name} \n Price: ${self.price} \n Weight: {self.weight} \n Brand: {self.brand} \n Status: {self.status} '
        )
        return self
    
item_1 = Product(150, 'Lebron 1', '2.5kg', 'Nike')
item_2 = Product(120, 'Durant 1', '2.5kg', 'Nike')
item_3 = Product(300, 'Curry 1', '2.5kg', 'Under Amour')
print('\n shoes 1 \n')
item_1.add_tax(0.15).sell().display_info()
print('\n shoes 2 \n')
item_2.return_item('defective').display_info()
print('\n shoes 3 \n')
item_3.display_info().add_tax(0.12).display_info()