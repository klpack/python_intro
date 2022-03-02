import math   # Importing Math

# Circle Class
class Circle(object):
    
    # Functions related to computation of area and perimeter
    def __init__(self,radius):
        self.radius = radius
       
    def area(self):
        return math.pi*(self.radius**2)
    
    def perimeter(self):
        return 2*math.pi*self.radius


# Calling circle size
small_circle = Circle(21)

# Output functions with format
print('\nThe area is: {:.3f}'.format(small_circle.area()))
print('\nThe perimeter is: {:.3f}'.format(small_circle.perimeter()))

