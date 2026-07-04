# age = 16
# citizen = False

# if age >= 18:
#    if citizen:
#       print("Eligible to vote.")
#    else:
#       print("Must be a Citizen to vote.")

# else:
#    print("Must be at least 18 years old to vote.")   

# balance = 15000
# withdraw = 10000

# if balance >= withdraw:
#    if withdraw <= 10000:
#       print("Transaction Successful")
#    else:
#       print("Withdrawal limit exceeded. Maximum allowed is Rs.10,000.")   
# else:
#    print("You don't have sufficent balance.")   

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license (yes/no) ?")

if age >= 18:
   if has_license == "yes":
      print("You can drive.")
   else:
      print("You need a driving license.")
else:
   print("You are underage.")   