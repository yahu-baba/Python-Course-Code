
# numbers = [1,2,2,3,3,4,5]

# unique = {num for num in numbers}

# print(unique)


# numbers = [1,2,3,4,5]

# unique = {n * n for n in numbers}

# print(unique)



# tuple_squares = tuple(x**2 for x in range(5))

# print(tuple_squares)



# numbers = [1,2,3,4,5]

# square_dict = {n:n*n for n in numbers}

# print(square_dict)



# students = ["Amit", "Rahul", "Priya"]

# length = {name:len(name) for name in students}

# print(length)


# words = ["apple","banana","apple","orange","banana","apple"]

# frequency = {word: words.count(word) for word in set(words)}

# print(frequency)


# students = [
#    ('Ravi',85), ('Sahil', 92), ('Priya', 78),
#    ('Sonam', 95), ('Rahul', 88)
# ]

# grade_book = {
#    name: 'A'
#    if score >= 90 else 'B'
#    if score >= 80 else 'C'
#    for name, score in students
# }

# print(grade_book)



# gen = (n*n for n in range(1,6))

# print(gen)

# print(list(gen))



# evens = (n for n in range(1,21) if n % 2 == 0)

# for num in evens:
#    print(num)



names = ["Amit", "Rahul", "Priya"]

upper = (name.upper() for name in names)

# print(list(upper))

for name in upper:
   print(name)
