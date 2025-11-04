class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def distance(self, other_circle):
        dx = self.x - other_circle.x
        dy = self.y - other_circle.y
        return (dx**2 + dy**2)**0.5

    def relationship(self, other_circle):
        dx = abs(self.x - other_circle.x)
        dy = abs(self.y - other_circle.y)
        d = self.distance(other_circle)
        
        if d < abs(self.radius - other_circle.radius):
            return "One circle is inside the other"
        
        elif d == abs(self.radius - other_circle.radius):
            return "Circles touch each other"

        elif d < self.radius + other_circle.radius:
            return "Circles intersect each other"
        
        else:
            return "Circles do not overlap"


x1 = float(input("Enter x-coordinate for circle 1: "))
y1 = float(input("Enter y-coordinate for circle 1: "))
radius1 = float(input("Enter radius for circle 1: "))


x2 = float(input("Enter x-coordinate for circle 2: "))
y2 = float(input("Enter y-coordinate for circle 2: "))
radius2 = float(input("Enter radius for circle 2: "))

c1 = Circle(x1, y1, radius1)
c2 = Circle(x2, y2, radius2)

relationship = c1.relationship(c2)
print(relationship)
