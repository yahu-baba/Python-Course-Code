
# for i in range(1, 11):
#    if i == 5:
#       break
#    print(i)

# print("Loop Finished")   


# fruits = ["Apple", "Mango", "Banana", "Orange"]

# search = "Mango"

# for fruit in fruits:
#    if fruit == search:
#       print("Fruit Found!")
#       break
# else:
#    print("Not Found.")   

# print("Searh Completed") 


correct_pin = "1234"

while True:
   pin = input("Enter PIN:")

   if pin == correct_pin:
      print("Login Successful")
      break

   print("Incorrect PIN")   