# Pattern : 1
# for a in range(1, 10):
#     for b in range(1, a + 1):
#         print("*", end=" ")
#     print()


# # Pattern : 2
# for a in range(1, 10):
#     for b in range(1, a + 1):
#         print(b, end=" ")
#     print()


# Pattern : 3
# for a in range(1, 6):
#     for b in range(1, a + 1):
#         print(a, end=" ")
#     print()


# Pattern : 4
num = 1

for a in range(1, 6):
    for b in range(1, a + 1):
        print(num, end=" ")
        num += 1
    print()    