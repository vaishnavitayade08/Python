import calendar
class leap_year:
    def __init__(self,year):
        self.year = year

    def leap_year(self):
        if (self.year % 100 ==0 and self.year % 400 == 0):
            print("year is leap yaer: ")
        elif (self.year % 4 ==0 and self.year % 100 !=0 ):
            print("year is leap year ")
        else:
            print("year is not a leap year")
    
year = int(input("Enter year: "))

obj = leap_year(year)
obj.leap_year()


