class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = [[0 for i in range(0,self.col)] for j in range(0,self.row)]

    def __str__(self):
        result = ""
        for i in range(0, self.row):
            result += str(self.value[i])
            result += "\n"
            
        return result
                
    def set(self, val):
        if self.row != len(val) or self.col != len(val[0]):
            return None

        for i in range(0, self.row):
            for j in range(0, self.col):
                self.value[i][j] = val[i][j]
        
    def transpose(self):
        result = Matrix(self.col, self.row)
        for i in range(0, self.col):
            for j in range(0, self.row):
                result.value[i][j] = self.value[j][i]

        return result
    
    def add(self, x):
        result = Matrix(self.row, self.col)
        if self.row != x.row or self.col != x.col:
            return None
        
        for i in range(0, len(self.value)):
            for j in range(0, len(self.value[i])):
                result.value[i][j] = self.value[i][j] + x.value[i][j]

        return result

    def sub(self, x):
        result = Matrix(self.row, self.col)
        if self.row != x.row or self.col != x.col:
            return None
        
        for i in range(0, len(self.value)):
            for j in range(0, len(self.value[i])):
                result.value[i][j] = self.value[i][j] - x.value[i][j]

        return result

    def mul(self, x):
        if self.col != x.row:
            return None
        
        result = Matrix(self.row, x.col)
        for i in range(0, result.row):
            for j in range(0, result.col):
                for k in range(0, self.col):
                    result.value[i][j] += self.value[i][k] * x.value[k][j]

        return result

    def __add__(self, x):
        result = Matrix(self.row, self.col)
        if self.row != x.row or self.col != x.col:
            return None
        
        for i in range(0, len(self.value)):
            for j in range(0, len(self.value[i])):
                result.value[i][j] = self.value[i][j] + x.value[i][j]

        return result

    def __sub__(self, x):
        result = Matrix(self.row, self.col)
        if self.row != x.row or self.col != x.col:
            return None
        
        for i in range(0, len(self.value)):
            for j in range(0, len(self.value[i])):
                result.value[i][j] = self.value[i][j] - x.value[i][j]

        return result

    def __mul__(self, x):
        if self.col != x.row:
            return None
        
        result = Matrix(self.row, x.col)
        for i in range(0, result.row):
            for j in range(0, result.col):
                for k in range(0, self.col):
                    result.value[i][j] += self.value[i][k] * x.value[k][j]

        return result
    

class SquareMatrix(Matrix):
    
    @staticmethod
    def identity(n):
        result = SquareMatrix(n)
        result.value = [[1 if i == j else 0 for j in range(0, n)] for i in range(0,n)]
        return result

    def __init__(self, size):
        self.size = size
        super().__init__(size, size)

    def isSymmetric(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.value[i][j] != self.value[j][i]:
                    return False
        return True

    def add(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[i+j for i,j in zip(self.value[k], x.value[k])] for k in range(0, self.size)]
        return result

    def sub(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[i-j for i,j in zip(self.value[k], x.value[k])] for k in range(0, self.size)]
        return result

    def mul(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[sum(a*b for a,b in zip(a_row, b_col)) for b_col in zip(*x.value)] for a_row in self.value]
        return result

    def pow(self, n):
        if isinstance(n, int) != True:
            return None
        if n < 0:
            return None
        else:
            result = SquareMatrix.identity(self.size)
            for i in range(0, n):
                result = result.mul(self)

            return result
        
    def __add__(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[i+j for i,j in zip(self.value[k], x.value[k])] for k in range(0, self.size)]
        return result

    def __sub__(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[i-j for i,j in zip(self.value[k], x.value[k])] for k in range(0, self.size)]
        return result

    def __mul__(self, x):
        result = SquareMatrix(self.size)
        if self.size != x.size:
            return None
        
        result.value = [[sum(a*b for a,b in zip(a_row, b_col)) for b_col in zip(*x.value)] for a_row in self.value]
        return result

    def __pow__(self, n):
        if isinstance(n, int) != True:
            return None
        if n < 0:
            return None
        else:
            result = SquareMatrix.identity(self.size)
            for i in range(0, n):
                result = result * self

            return result
        
x=Matrix(4,3)
y=Matrix(4,3)
z=Matrix(3,4)
x.set([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y.set([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
z.set([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"x = \n{x}")
print(f"y = \n{y}")
print(f"z = \n{z}")
print(f"x.add(y) = \n{x.add(y)}")
print(f"x.sub(y) = \n{x.sub(y)}")
print(f"x.mul(z) = \n{x.mul(z)}")
print(f"x+y = \n{x+y}")
print(f"x-y = \n{x-y}")
print(f"x*z = \n{x*z}")
a=SquareMatrix(3)
a.set([[1,2,3],[4,5,6],[7,8,9]])
b=SquareMatrix(3)
b.set([[0,2,0],[2,0,2],[0,2,0]])
print(f"a = \n{a}")
print(f"b = \n{b}")
print(f"a.add(b) = \n{a.add(b)}")
print(f"a.sub(b) = \n{a.sub(b)}")
print(f"a.mul(b) = \n{a.mul(b)}")
print(f"a+b = \n{a+b}")
print(f"a-b = \n{a-b}")
print(f"a*b = \n{a*b}")
print(f"a is symmetric matrix? {a.isSymmetric()}")
print(f"b is symmetric matrix? {b.isSymmetric()}")
print()
for i in range(0, 11):
    print(f"b.pow({i}) = \n{b.pow(i)}")
    
for i in range(0, 11):
    print(f"b ** {i} = \n{b ** i}")
    
