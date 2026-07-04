# per = float(input("Enter Score : "))

# if per >= 80 and per <= 100:
#    print("Merit")
# elif per >= 60 and per < 80:
#    print("Ist Division")   
# elif per >= 45 and per < 60:
#    print("IInd Division")
# elif per >= 33 and per < 45:
#    print("IIIrd Division") 
# elif per < 33:
#    print("Fail")  
# else:
#    print("Enter the correct percentage.")           

# age = int(input("Enter Age : "))

# if age < 13:
#    print("Child")
# elif age < 20:
#    print("Teenager")   
# elif age < 60:
#    print("Adult")
# else:
#    print("Senior Citizen")

username = input("Enter UserName : ")
password = input("Enter Password : ")

if username != "admin":
   print("Invalid Username")
elif password != "1234": 
   print("Invalid password")
else:
   print("Login Successful") 