class misc:
    def __init__(self,a,b,list1):
        self.a = a
        self.b = b
        self.list1 = list1
    
    def add(self):
        return self.a + self.b
    
    def addlist(self):
        return sum(self.list1)
    
    def maxnum(self):
        return max(self.a,self.b)
    
    def maxternary(self):
        mxnum = self.a if self.a > self.b else self.b
        return mxnum
    
    def maxsort(self):
        list2 = [self.a,self.b]
        list2.sort()
        return (list2[-1])
    
    
obj = misc(5,15,[1,3,3])
print(obj.add())
print(obj.addlist())
print(obj.maxnum())
print(obj.maxternary())
print(obj.maxsort())



