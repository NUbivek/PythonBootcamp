# Make a class called Vector2D
# Assume that the vectors go from the origin to some point X, Y Vectors should have the following methods
# addition subtraction absolute value (same as distance from the origin to X, Y)
# Should also have methods that can check if two vectors are equal or not equal (ne) Finally, Vector2D should have a str method to print itself


class Vector2D():

	def __init__(self, x, y):

		self.x = x
		self.y = y
	
	def __str__(self):
		return "The x and y points are: x is {} and y is {}.".format(self.x,self.y)


	def __add__(self, other):
		
		self.x += other.x
		self.y += other.y
		return"x is {} and y is {}".format(self.x, self.y)

	def __sub__(self,other):

		self.x -= other.x
		self.y -= other.y
		return "x is {} and y is {}".format(self.x, self.y)

	def __abs__(self):

		self.x = abs(self.x)
		self.y = abs(self.y)
		return "x is {} and y is {}".format(self.x, self.y)

v1 = Vector2D(3,4)

v2 = Vector2D(-5,-9)
#v2.__abs__()

print(v1)
print(v2)
#print("absolute",o1)

# print (v1)

#sub_abs_xy = absolute(self.x - self.y)

