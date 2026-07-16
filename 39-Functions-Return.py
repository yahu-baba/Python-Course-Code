
# def add(a, b):
#    result = a + b
#    return result

# sum = add(10, 20)

# print(sum)


# def check_even(number):
#    if number % 2 == 0:
#       return "Even"
#    else:
#       return "Odd"

# print(check_even(15))      
# print(check_even(28))      

def total(numbers):
   result = 0

   for num in numbers:
      result += num

   return result 

def percentage(allMarks):
   per =  (total(allMarks) / 400) * 100
   return per

marks = [85, 90, 78, 92]

print(percentage(marks), "%")