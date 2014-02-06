class Vector:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        """
        Defines how <self> * <other> behaves

        """
        if type(other) == int or type(other) == float:
            return Vector(self.x * other,
                          self.y * other,
                          self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + \
                   self.y * other.y + \
                   self.z * other.z
        else:
            raise TypeError()

    def __rmul__(self, other):
        """
        Defines how <other> * <self> behaves; note that the arguments appear
        in reverse order in the function definition.

        """
        return self.__mul__(other)

    def __str__(self):
        """
        Defines how instances of the Vector class are printed to the console

        """
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)


class Matrix:
    def __init__(self, m, n):
        """
        Construct a zero matrix with m rows and n columns

        """
        self.m = m
        self.n = n
        self.values = []
        for _ in xrange(m):
            self.values.append([0] * n)

    def __getitem__(self, other):
        """
        Define how <self>[<other>] behaves (e.g. matrix[1])

        """
        return self.values[other]

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = Matrix(self.m, self.n)
            for i in xrange(m):
                for j in xrange(n):
                    result[i][j] = other * self[i][j]
            return result
        else:
            if self.n != other.m:
                raise ValueError("Incompatible matrix dimensions")
            result = Matrix(self.m, other.n)
            # i and j iterate over each entry of the result.  Each entry of the
            # result is calculated by indexing over the row/column entries of
            # self/other (respectively).  k achieves the row/column indexing
            for i in xrange(result.m):
                for j in xrange(result.n):
                    for k in xrange(self.n):
                        result[i][j] += self[i][k] * other[k][j]
            return result
