# 4. Shape Class with Subclasses for Different Shapes : W3Resources
# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shapes:
  def getArea(self):
    pass
  def getPerim(self):
    pass
class Circle(Shapes):
  def __init__(self, radius):
    self.radius = radius
  def getArea(self):
    return math.pi*(self.radius**2)
  def getPerim(self):
    return 2*math.pi*self.radius
class Triangle(Shapes):
  def __init__(self, base, height, a, b, c):
    self.base = base
    self.height = height
    self.a = a
    self.b = b
    self.c = c
  def getArea(self):
    return (1/2) * self.base * self.height
  def getPerim(self):
    return self.a + self.b + self.c
class Rectangle(Shapes):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def getArea(self):
    return self.width*self.height
  def getPerim(self):
    return (2*self.width)+(2*self.height)

r = 7
circle = Circle(r)
circle_area = circle.getArea()
circle_perimeter = circle.getPerim()

print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)

r
w = 5
h = 7
rectangle = Rectangle(w, h)
rectangle_area = rectangle.getArea()
rectangle_perimeter = rectangle.getPerim()


print("\nRectangle: Width =", w, " Height =", h)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.getArea()
triangle_perimeter = triangle.getPerim()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)
    