##convert kilometers to mile
class convert():
    def __init__(self,km,cel):
        self.km = km
        self.cel = cel
        
    
    def km_to_mile(self):
        conversion_factor = 0.621371
        mile =  self.km * conversion_factor
        print(" km to mile is: ",mile)

    def cel_to_far(self):
        far = (self.cel * 9/5) + 32
        print("cel to far: ", far)

km = float(input("Enter km: "))
cel = float(input("enter cel: "))

obj = convert(km,cel)
obj.km_to_mile()
obj.cel_to_far()

        
    

