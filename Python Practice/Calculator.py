# 3. Calculator Class for Basic Arithmetic Operations : W3Resources
# Write a Python program to create a calculator class. 
# Include methods for basic arithmetic operations.

class Calc:
  def add(self, x, y):
    return x+y
  def subtract(self, x, y):
    return x-y
  def divide(self, x, y):
    return x/y
  def multiply(self, x, y):
    return x*y
  def mod(self, x, y):
    return x%y

x = 20
y = 4
calc = Calc()

print("x + y = ", calc.add(x,y), ", x - y = ", calc.subtract(x,y), ", x / y = ", calc.divide(x,y), ", x * y = ", calc.multiply(x,y), ", x % y = ", calc.mod(x,y))