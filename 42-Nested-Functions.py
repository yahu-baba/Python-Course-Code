
def outer():
   print("Inside Outer Function")

   message = "welcome"

   def inner():
      print("Inside Inner Function")
      print(message)

   inner()


outer()



# def calculator(a, b):

#    def add():
#       return a + b 
   
#    def subtract():
#       return a - b

#    print("Addition :", add())   
#    print("Subtraction :", subtract())   

# calculator(20, 5)


# def login(username, password):

#    def validate():
#       return username == "admin" and password == "1234"

#    if validate():
#       print("Login Successful")  
#    else:
#       print("Invalid Credentials")   


# login("admin", "1234")
# login("rahul", "1234")