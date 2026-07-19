
# def greet():
#    message = "Hello"
#    print(message)

# greet()



# count = 10

# def display():
#    global count
#    count = count + 1
#    print(count)
   
# display()
# print(count)   


def outer():
   number = 10

   def inner():
      nonlocal number
      number = number + 1
      print(number)

   inner()   

outer()   
outer()   
outer()   