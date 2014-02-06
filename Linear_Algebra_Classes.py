class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mult__(self, other):
        return Vector(other*self.x, other*self.y)
    def __str__(self):
        return str((self.x,self.y))
    def norm(v):
        return v.x*v.x + v.y*v.y


class Matrix(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Matrix(self.x + other.x, self.y + other.y)
    def __str__(self):
        return str(((self.x.x, self.x.y), (self.y.x, self.y.y)))
    def __mul__(self, other):
        return Matrix(self.x * other.x.x + self.y * other.x.y, self.x * other.y.x + self.y * other.y.y)
    def multiply(self, vector):
        return self.x * vector.x + self.y * vector.y

    
    
        
