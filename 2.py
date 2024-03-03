import math

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Line(Point):
    def __init__(self, point1, point2):
        self.point1=point1
        self.point2=point2
        
    def length(self):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2=self.point2.x, self.point2.y
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
class Triangle(Line):
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        
    def perimeter(self):
        return self.line1.length() + self.line2.length() + self.line3.length()
        
point1 = Point(0, 3)
point2 = Point(3, 1)
line = Line(point1, point2)
print("Довжина лінії:", line.length())
line1 = Line(point1, point2)
line2 = Line(point2, Point(4, 0))
line3 = Line(Point(4, 0), Point(5, 3))
triangle = Triangle(line1, line2, line3)
print("Периметр трикутника:", triangle.perimeter())