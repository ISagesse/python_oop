# Now, let's build a store to contain our products by making a store class and putting our products into an array.

class Store:
    def __init__(self, owner, location):
        self.products = []
        self.owner = owner
        self.location = location
        
    def add_product(self, lst):
        self.products.append(lst)
        return self
    
    #this will remove an item by name
    def remove_product(self, item_to_remove):
        for item in self.products:
            #searching by item name
            if item[1] == item_to_remove:
                #if found this item remove that list
                self.products.remove(item)
                
    def inventory(self):
        for item in self.products:
            print(item)
        
        #return self for chaining methods
        return self
    
store_1 = Store('Israel', 'Miami')
store_1.add_product([150, 'Lebron 1', '2.5kg', 'Nike']).add_product([120, 'Durant 1', '2.5kg', 'Nike']).add_product([300, 'Curry 1', '2.5kg', 'Under Amour'])
print('\n Remove an item')
store_1.inventory().remove_product('Durant 1')
print('\n New inventory')
store_1.inventory()
