class Vector:
    name = "Vector"
    
    @staticmethod
    def zeros(n):
        return Vector([0 for i in range(0,n)])

    @classmethod
    def intro(cls):
        print(f"Hello, I'm {cls.name}")
        
    def __init__(self, x):
        if isinstance(x, list) or isinstance(x, tuple):
            self.value = x

    def __add__(self, other):
        if len(self.value) != len(other.value):
            return None
        else:
            return [x+y for x,y in zip(self.value,other.value)]

    def __sub__(self, other):
        if len(self.value) != len(other.value):
            return None
        else:
            return [x-y for x,y in zip(self.value,other.value)]

    def __mul__(self, other):
        if isinstance(other, list) or isinstance(other, tuple) or isinstance(other, Vector):
            if len(self.value) != len(other.value):
                return None
            else:
                return [x*y for x,y in zip(self.value,other.value)]
        elif isinstance(other, int) or isinstance(other, float):
            return [x*other for x in self.value]

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return [x*other for x in self.value]
        else:
            return none

    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                return None
            else:
                return [x/other for x in self.value]
        else:
            return None

    def __str__(self):
        return f"{self.value}"

    def __len__(self):
        return len(self.value)
        
a = Vector([1,2,3])
b = Vector([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(3*a)
print(a*3)
print(a/3)

