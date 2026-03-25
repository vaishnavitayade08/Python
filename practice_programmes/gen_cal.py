import calendar
class cal:
    def __init__(self,month,year):
        self.month = month
        self.year = year

    def cal_gen(self):
        cal_display = calendar.month(self.year,self.month)
        print(cal_display)
        return cal_display
    
month = int(input("Enter month: "))
year = int(input("Enter year: "))

obj = cal(month,year)
obj.cal_gen()
