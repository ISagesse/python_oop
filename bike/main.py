class Bike:
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        
    def display_info(self):
        print(f'Bike price: ${self.price}, Max speed: {self.max_speed}mph, Miles: {self.miles} ')
        
    def ride(self):
        self.miles += 10
        print('Riding')
        return self
        
    def reverse(self):
        if self.miles > 0: 
            self.miles -= 5
            print('Reversing')
        else:
            print('cannot reverse')
        return self
        
bike_1 = Bike(100, 25)
bike_2 = Bike(150, 35)
bike_3 = Bike(300, 55)

bike_1.ride().ride().ride().reverse().display_info()

bike_2.ride().ride().reverse().reverse().display_info()

bike_3.reverse().reverse().reverse().display_info()