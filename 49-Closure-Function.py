
# def outer():
#    message = "hello Python"

#    def inner():
#       print(message)

#    return inner   

# test = outer()
# test()


# def greeting(name):

#    def say_hello():
#       print(f"Hello {name}")

#    return say_hello

# person1 = greeting("Amit")   
# person2 = greeting("Rahul")   

# person1()
# person2()


# def counter():
#    count = 0

#    def increment():
#       nonlocal count
#       count += 1
#       print(count)

#    return increment  

# c = counter() 

# c()
# c()
# c()



def multiply_by(x):

   def multiply(y):
      return x * y
   
   return multiply

double = multiply_by(2)  
triple = multiply_by(3)  


print(double(10))
print(triple(10))