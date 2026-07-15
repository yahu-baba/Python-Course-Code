# Pattern 1
# rows = 5

# for a in range(rows):
#     for b in range(rows):
#         if a == 0 or a == rows - 1 or b == 0 or b == rows - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# Pattern 2
# rows = 5

# for a in range(rows):
#     # Print spaces
#     for s in range(rows - a - 1):
#         print(" ", end="")

#     # Print stars
#     for b in range(2 * a + 1):
#         print("*", end="")

#     print()


# Pattern 3
# rows = 5

# for a in range(rows):
#     for s in range(rows - a - 1):
#         print(" ", end="")

#     for b in range(2 * a + 1):
#         if b == 0 or b == 2 * a or a == rows - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()



# Pattern 4
rows = 7

for a in range(rows):
    for b in range(rows):
        if a == b or a + b == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

