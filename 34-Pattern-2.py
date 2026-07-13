# Pattern : 1
# for a in range(10, 0, -1):
#     for b in range(a):
#         print("*", end=" ")
#     print()


# Pattern : 2
# for a in range(10, 0, -1):
#     for b in range(1, a+1):
#         print(b, end=" ")
#     print()


# Pattern : 3
# for a in range(5, 0, -1):
#     for b in range(a):
#         print(a, end=" ")
#     print()


# Pattern : 4
# for a in range(5, 0, -1):
#     for b in range(a, 0, -1):
#         print(b, end=" ")
#     print()


# Pattern : 5
num = 1

for a in range(5, 0, -1):
    for b in range(1, a + 1):
        print(num, end=" ")
    print()
    num += 1