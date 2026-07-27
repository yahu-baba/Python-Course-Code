# def decorator(func):

#     def wrapper(name):
#         print("Before")

#         func(name)

#         print("After")

#     return wrapper

# @decorator
# def hello(name):
#     print(f"Hello {name}")

# hello("Sanchit")



# def decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Starting....")

#         result = func(*args, **kwargs)

#         print("Finished.")

#         return result

#     return wrapper

# @decorator
# def add(a, b):
#     return a + b

# print(add(10, 20))




logged_in = False

# def login_required(func):

#    def wrapper():
#       if logged_in:
#          func()
#       else:
#          print("Please Login")

#    return wrapper
      
# @login_required
# def dashboard():
#    print("welcome to Dashboard")

# dashboard()   




def stars(func):
   def wrapper():
      print("*************")
      func()
      print("*************")
   return wrapper       

def welcome(func):
   def wrapper():
      print("welcome")
      func()

   return wrapper   

@stars
@welcome
def hello():
   print("Hello")

hello() 