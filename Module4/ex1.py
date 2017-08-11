# Make a class called Point
# each point should have two attributes, X and Y

# each point should have a 'reset' method that works as follows:
#     if p1 is a Point, then
#     p1.reset() should make X = 0 and Y = 0 for that point

# each point should have a __str__ method that prints the X and Y coordinates of the point

# each point should have a 'move' method that works as follows:
#     if p1 is a Point, then
#     p1.move(new_X, new_Y) should make X = new_X and Y = new_Y

# each point should have a 'distance' method that works as follows:
#     if p1 and p2 are both Points, then
#     p1.distance(p2) = equals the distance of the line joining the two points

class Point():

	def __init__(self,x=0,y=0):

		self.x = x
		self.y = y

	def reset(self):
		self.x = 0
		self.y = 0

	def __str__(self):
		return "The x and y points are: x is {} and y is {}.".format(self.x,self.y)

	def move(self, new_x, new_y):
		self.x += new_x
		self.y += new_y
		

	def distance(self, other):
		
		from math import sqrt
		distance = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
		return distance
#pl = Point(8,9)

P1 = Point(7,3)
P2 = Point(6,9)
#pl.reset()
#pl.move(2,3)
d = P1.distance(P2)

print(d)

# print(pl)
# print(distance)




