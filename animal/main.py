# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print(self.health)
        return self
    
class Dog(Animal):
    def __init__(self):
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self
    
class Dragon(Animal):
    def __init__(self):
        self.health = 170
        
    def fly(self):
        self.health -= 10
        return self
        
    def display_health(self):
        print('I am dragon')
        return super().display_health()
        
        
a = Animal('John', 20)
a.display_health()

b = Dragon()
b.walk().walk().walk().fly().fly().display_health()