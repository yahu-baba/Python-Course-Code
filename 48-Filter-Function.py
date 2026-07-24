
# numbers = [1,2,3,4,5,6,7,8]

# def even(n):
#    return n % 2 == 0

# result = filter(even, numbers)   

# print(list(result))



# ages = [12, 18, 25, 14, 40]

# result = filter(lambda age: age >= 18, ages )

# print(list(result))



# words = ["cat", "elephant", "dog", "python", "AI"]

# result = filter(lambda word: len(word) > 3, words)

# print(list(result))



# emails = [
#    "amit@gmail.com",
#    "rahul",
#    "admin@yahoo.com",
#    "hello"
# ]

# result = filter(lambda email: "@" in email, emails)

# print(list(result))


salary = [18000, 25000, 32000, 15000, 50000]

eligible = filter(lambda s: s >= 20000, salary)

bonus = map(lambda s: s + 5000, eligible)

print(list(bonus))

