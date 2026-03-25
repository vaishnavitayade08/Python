class facto_num:
    def __init__(self,num,factorial):
        self.num = num
        self.factorial = factorial

    def fact_num(self):
        if self.num < 0 :
            print("num is negative")
        elif self.num == 0:
            print("num is 0")
        else:
            for i in range(1,self.num+1):
                self.factorial = self.factorial * i
                print(self.factorial)
            

num = int(input("enter num: "))
factorial = 1
obj = facto_num(num, factorial)
obj.fact_num()


