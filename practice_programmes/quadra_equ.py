##𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0 = (−𝑏 ± (𝑏 − 4𝑎𝑐 )/(2𝑎)

import math
class quad_equ:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    
    def solution(self):
        descri = self.b**2 - self.a * self.c * 4
        if descri > 0:
            root1 = (-self.b + math.sqrt(descri)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(descri)) / (2 * self.a)
            print("roots are: ",root1, root2)

        elif descri== 0:
            root = - self.b /  (2 * self.a)
            print("root is: ",root)
        else:
            real_part = - self.b / (2 * self.a)
            img_part = math.sqrt(abs(descri)) / (2 * self.a)
            root1 = real_part + img_part
            root2 = real_part - img_part
            print("roots are: ",root1,root2)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

obj = quad_equ(a,b,c)
obj.solution()

        





    