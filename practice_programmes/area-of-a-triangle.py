def area_of_triangle(base, height):
    area  = (base * height)/2
    return area
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of traingle: "))
result = area_of_triangle(base, height)
print("area of traingle: ",result)
