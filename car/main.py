# Create a class called  Car. Allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
            
        self.display_all()
            
    def display_all(self):
        print(
            f'Price: {self.price} \nSpeed: {self.speed} \nFuel: {self.speed} \nMileage: {self.mileage} \nTax: {self.tax} '
        )
        
car_1 = Car(2000, '35mph', 'Full', '15mpg')
car_2 = Car(2000, '5mph', 'Not Full', '105mpg')
car_3 = Car(2000, '15mph', 'Kind of full', '95mpg')
car_4 = Car(2000, '25mph', 'Full', '25mpg')
car_5 = Car(2000, '45mph', 'Empty', '25mpg')
car_6 = Car(20000000, '35mph', 'Empty', '15mpg')

