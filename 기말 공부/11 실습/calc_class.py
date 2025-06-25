class Calc:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def foo(self):
        print("Calc class")

    def bar(self):
        print(f"first = {self.first}, second = {self.second}")

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


class MyCalc(Calc):
    name = "MyCalc"

    @classmethod
    def blahblah(cls):
        print("Blahblah")
        
    @classmethod
    def introduce(cls):
        print(f"This is {cls.name}")
        print("Added quot, mod, and pow methods.")
        cls.blahblah()
    
    def __init__(self):
        super().__init__(0,0)
        
    def quot(self):
        if self.second == 0:
            return 0
        else:
            return self.first // self.second

    def mod(self):
        if self.second == 0:
            return 0
        else:
            return self.first % self.second

    def pow(self):
        return self.first ** self.second

    def div(self):
        if self.second == 0:
            return None
        else:
            return super().div() #부모클래스의 기능을 그대로 사용
