
# sum = lambda a, b: a + b

# print(sum(10, 20))
# print(sum(15, 20))

# square = lambda x: x * x

# print(square(4))
# print(square(5))


# cube = lambda x: x ** 3 

# print(cube(2))


# maximum = lambda a, b: a if a > b else b

# print(maximum(15, 30))
# print(maximum(45, 30))



# numbers = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x * x, numbers))

# print(result)  



numbers = [10, 15, 18, 21, 30]

even = filter(lambda x: x % 2 == 0, numbers)

print(list(even))