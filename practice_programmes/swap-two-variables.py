class swap_num:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def swap_num(self):
        self.a ,self.b = self.b, self.a
        return self.a, self.b

a = int(input("Enter a: "))
b = int(input("Enter b: "))
obj = swap_num(a,b)
print("value of a & b:", obj.swap_num())




