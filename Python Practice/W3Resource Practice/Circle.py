# 1. Circle Class for Area and Perimeter : W3Resources
# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.
import math

class Circle:
  def __init__(self, radius):
    self.radius = radius
    
  def getArea(self):
    return math.pi * self.radius**2
    
  def getPerimeter(self):
    return 2*math.pi*self.radius
  
  
radius = float(input("Enter a radius for your circle: "))
circle = Circle(radius)

area = circle.getArea()
perimeter = circle.getPerimeter()

print("The circle has an area of: ", area, " and a perimeter of: ", perimeter)
    