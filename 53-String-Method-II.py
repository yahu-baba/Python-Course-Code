
# print("Python@123".isalnum())

# print("Python Language".isalpha())

# print("1234.45".isdigit())

# print("python1234".islower())

# print("PYTHOn 1234".isupper())

# print(" Hello ".isspace())


# text = "Python"

# print(text.center(20, "*"))

# print(text.ljust(20, "*"))

# print(text.rjust(20, "-"))

# number = "-25"

# print(number.zfill(5))


name = "John"
age = 25

# print("Name : {}, Age : {}".format(name, age))

# print("Name : {1}, Age : {0}".format(name, age))

# print("|{:^10}|".format("Python"))
# print("|{:<10}|".format("Python"))
# print("|{:>10}|".format("Python"))

student = {
   "name" : "John",
   "age" : 22,
   "city" : "London"
}

text = "{name} is {age} years old and lived in {city}"

print(text.format_map(student))