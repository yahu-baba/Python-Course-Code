
# def numbers(*args):
#    for num in args:
#       print(num)

  
# numbers(10, 20, 30)   


# def total(*numbers):
#    result = 0

#    for num in numbers:
#       result += num

#    return result   

  
# print(total(10, 20, 30) )
# print(total(30, 65) )


def students(message,*names):
   print("Student List:")

   for name in names:
      print(message, name)

students("Hello","Rahul", "Priya","Amit", "Neha")