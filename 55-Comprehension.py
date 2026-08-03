# numbers = [1,2,3,4,5]

# squares = [num **2 for num in numbers]

# print(squares)



# names = ["amit", "rahul", "priya"]

# # upper = [name.upper() for name in names]
# upper = [len(name) for name in names]

# print(upper)



# numbers = [1,2,3,4,5,6,7,8]

# evens = [num for num in numbers if num % 2 != 0]

# print(evens)



# text = "A1B2C3D4"

# digits = [ch for ch in text if ch.isdigit()]

# print(digits)




# numbers = range(1, 11)

# result = [n ** 2 for n in numbers if n % 2 == 0]

# print(result)




# marks = [34, 67, 90, 23, 56]

# status = ["Pass" if m >= 40 else "Fail" for m in marks]

# print(status)



matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
         ]

# flat = [num for row in matrix for num in row]         

# print(flat)


flat = []

for row in matrix:
   for num in row:
      flat.append(num)

print(flat)      