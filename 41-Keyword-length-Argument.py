
# def student(**kwargs):
#    for key, value in kwargs.items():
#       print(key, ":", value)
 
# student(name="Sanchit", age=25, city="Mumbai")   


# def display(*args, **kwargs):

#    print("Positional Arguments :")

#    for value in args:
#       print(value)

#    print()   

#    print("Keyword Arguments :")

#    for key, value in kwargs.items():
#       print(key, ":", value)

# display(10, 
#         20, 
#         30, 
#         name="Sanchit", 
#         age=22, 
#         city="Delhi"
#       )      



def demo(name, age, *skills, **details):
   pass

demo("Rahul", 22, "python", "C++", "Java", city= "Delhi", salary=50000 )