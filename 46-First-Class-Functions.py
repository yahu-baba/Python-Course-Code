
# def greet():
#    print("hello")

# a = greet   
# b = greet   
# c = greet   

# a()
# b()
# c()

# message = greet   

# # message()
# print(type(message))


# def add():
#    print("Addition")

# def subtract():
#    print("Subtraction")   

# def multipy():
#    print("Multiplication") 

# items = (10, "Python", add, subtract)

# items[2]()
# items[3]()

# print(items[0])


# operations = {
#    "add" : add,
#    "subtract" : subtract,
#    "multipy" : multipy
# }   

# operations["subtract"]()

# operations = [add, subtract, multipy]   

# for operation in operations:
#    operation()


# def greet():
#    print("Good Morning")

# def execute(function):
#    function()   

# execute(greet)   



def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def calculate(operation, x, y):
   return operation(x, y)

print(calculate(add, 10, 20))  
print(calculate(subtract, 20, 8))  