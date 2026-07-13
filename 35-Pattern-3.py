# rows = 5

# for a in range(1, rows + 1):
#     # Spaces
#     for s in range(rows - a):
#         print(" ", end=" ")

#     # Stars
#     for b in range(a):
#         print("*", end=" ")

#     print()


# Pattern 2
# rows = 5

# for a in range(1, rows + 1):
#     # Spaces
#     for s in range(rows - a):
#         print(" ", end=" ")

#     # Number
#     for b in range(1, a+1):
#         print(b, end=" ")

#     print()


#Pattern 3
# rows = 5

# for a in range(1, rows + 1):
#     # Spaces
#     for s in range(rows - a):
#         print(" ", end=" ")

#     # Number
#     for b in range(1, a+1):
#         print(a, end=" ")

#     print()


# Pattern 4
# rows = 5

# for a in range(rows, 0, -1):
#     # Spaces
#     for s in range(0, rows - a):
#         print(" ", end=" ")

#     # Stars
#     for b in range(a):
#         print("*", end=" ")

#     print()


# # Pattern 5
# rows = 5

# for a in range(rows, 0, -1):
#     # Spaces
#     for s in range(0, rows - a):
#         print(" ", end=" ")

#     # Numbers
#     for b in range(1, a + 1):
#         print(b, end=" ")

#     print()


# # Pattern 6
# rows = 5

# for a in range(rows, 0, -1):
#     # Spaces
#     for s in range(0, rows - a):
#         print(" ", end=" ")

#     # Numbers
#     for b in range(1, a + 1):
#         print(a, end=" ")

#     print()


# Pattern 7
rows = 5

for a in range(rows, 0, -1):
    # Spaces
    for s in range(rows - a):
        print(" ", end=" ")

    # Numbers
    for b in range(a, 0, -1):
        print(b, end=" ")

    print()