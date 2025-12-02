# 8. Shopping Cart Class : W3Resources
# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class Item:
    def __init__(self, product, price):
        self.name = product
        self.price = price

class Cart:
    def __init__(self, item=None):
        self.items = []
        self.size = 0
        self.price = 0
        
        if item is not None:
          self.items.append(item)
          self.size = 1
          self.price += item.price
    def addItem(self, item):
        self.items.append(item)
        self.size += 1
        self.price += item.price
    def removeItem(self, item):
        if len(self.items) == 0:
          return 0
        self.items.remove(item)
        self.size -= 1
        self.price -= item.price
    def checkout(self):
        return self.price
    def printCart(self):
        for i in self.items:
            print(i.name, ": ", str(i.price))
        print("Cart Total =",self.price)
    def printC(self):
      output = ''
      for i in self.items:
        output += (i.name + ": " + str(i.price) + ", ")
      return output
    
cart1 = Cart()
item1 = Item("Carrots", 2.30)
cart2 = Cart(item1)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

item2 = Item("ramen", 8.67)
cart1.addItem(item2)
cart2.addItem(item2)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

item3 = Item("bacon", 5.47)
cart1.addItem(item3)
cart2.addItem(item3)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

item4 = Item("4K OLED TV", 329.99)
cart1.addItem(item4)
cart2.addItem(item4)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())


print("Test cart1.printCart():")
cart1.printCart()
print("Test cart2.printCart():")
cart2.printCart()

print("Test removeItem() function:")



cart2.removeItem(item1)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

cart1.removeItem(item2)
cart2.removeItem(item2)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

cart1.removeItem(item3)
cart2.removeItem(item3)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())

cart1.removeItem(item4)
cart2.removeItem(item4)
print("cart1 =", cart1.printC(), "- cart2 =", cart2.printC())