# day = int(input("Enter weekday :"))

# match day:
#    case 1:
#       print("Monday")
#    case 2:
#       print("Tuesday")   
#    case 3:
#       print("wednesday")   
#    case 4:
#       print("Thursday")   
#    case 5:
#       print("Friday")   
#    case 6 | 7:
#       print("weekend")   
#    case _:
#       print("Enter the correct Week Day.")   


# A = float(input("Value of A :"))
# B = float(input("Value of B :"))
# operator = input("Operator :")

# match operator:
#    case "+":
#       print(A + B)
#    case "-":
#       print(A - B)   
#    case "*":
#       print(A * B)   
#    case "/":
#       print(A / B)   
#    case _:
#       print("Invalid Operator.") 

# month = input("Enter Month :")

# match month:
#    case "December" | "January" | "February":
#       print("winter")
#    case "March" | "April" | "May":
#       print("Summer")   
#    case "June" | "July" | "August":
#       print("Rainy")   
#    case "September" | "October" | "November":
#       print("Autumn")   
#    case _:
#       print("Invalid Month")

# data = [20, 10]

# match data:
#    case [10, 20]:
#       print("Both Numbers Found")
#    case [10]:
#       print("Only One Number")   
#    case _:
#       print("Unknown Data")

# point = (22, 0)

# match point:
#    case (0, 0):
#       print("Origin")

#    case (0, y):
#       print("Y Axis:", y) 

#    case (x, 0):
#       print("X Axis:", x)
#   
#    case (x, y):
#       print("Point:", x, y)         
   
# student = {
#    "name" : "Sanchit",
#    "age" : 25
# }

# match student:
#    case {"name": name, "age": age}:
#       print(name)
#       print(age)

#    case _:
#       print("Invalid Data") 


# age = 88

# match age:
#    case x if x < 13:
#       print("Child")
#    case x if x < 20:
#       print("Teenager")
#    case x if x < 60:
#       print("Adult")   
#    case _:
#       print("Senior Citizen") 

point = (0, 33)

match point:
   case (_, 20):
      print("Second value is 20")
   
   case _:
      print("No Match")