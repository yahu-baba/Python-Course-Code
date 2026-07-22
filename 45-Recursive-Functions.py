
# def print_numbers(n):

#    if n > 5:
#       return

#    print(n)

#    print_numbers(n + 1)

# print_numbers(2)   



# def countdown(n):

#    if n == 0:
#       print("Done")
#       return

#    print(n)

#    countdown(n - 1)

# countdown(5)   



# def factorial(n):

#     if n == 1:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(10))



def reverse(text):

    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]

print(reverse("Python is Good"))
