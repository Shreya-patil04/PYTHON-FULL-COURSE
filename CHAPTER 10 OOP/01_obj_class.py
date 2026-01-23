# procuderal oriented programming
a = 12
b = 13
c = a + b
print(c)

# object oriented programming
class Number:
    def sum(self):
        return self.a + self.b
    
num = Number()
num.a = 12
num.b = 13
result = num.sum()
print(result)

# example for class and object
class RailywayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harryApplication = RailywayForm()
harryApplication.name = "Harry"
harryApplication.train = "Rajdhani Express"

# Game example
class Remote():
    pass
class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveUp(self):
        pass

player1 = Player() # create object of player
remote1 = Remote() # create object of remote

if(remote1.pressed()): # if remote's left button is pressed
    player1.moveLeft() # move player to left

