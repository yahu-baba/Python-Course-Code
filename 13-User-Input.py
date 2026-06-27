# name = input("Enter your name : ")
# city = input("Enter your city : ")

# print("Hello My name is", name, end= " ")
# print("I am from", city)

# print(f"My name is {name} and city {city}")

# width = float(input("Enter width : "))
# height = float(input("Enter Height : "))

try:
   width = int(input("Enter width : "))
   height = int(input("Enter Height : "))
except ValueError:
   print("Please enter a valid number")   

area = width * height

print("Area of rectange =", area)