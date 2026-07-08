# rows = 4
# cols = 6

# i = 1
# while i <= rows:
#     j = 1
#     while j <= cols:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1

# num = 1

# while num <= 5:
   
#    i = 1
#    while i <= 10:
#       print(f"{num} x {i} = {num * i}")
#       i += 1

#    print("-" * 20)  
#    num += 1 


# board = [
#    ["X", "O", "X"],
#    ["O", "X", "O"],
#    ["X", "O", "X"]
# ]

# i = 0

# while i < len(board):
#    j = 0
#    while j < len(board[i]):
#       print(board[i][j], end=" ")
#       j += 1
#    print()   
#    i += 1


students = ["Amit", "Rahul", "Priya"]

marks = [
    { "Math" : 58, "Science": 67, "English" : 84 },
    { "Math" : 88, "Science": 77, "English" : 89 },
    { "Math" : 67, "Science": 75, "English" : 79 },
] 

i = 0

while i < len(students):
   print("Student Name :", students[i])

   subjects = list(marks[i].items())
   
   j = 0
   while j < 3:
       subject, score = subjects[j]
       print(subject, ":" ,score)
       j += 1
   print("-" * 20)    
   i += 1

