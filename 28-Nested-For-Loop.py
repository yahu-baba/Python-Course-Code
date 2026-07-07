# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# rows = 10
# num = 1

# for i in range(rows):
#     for j in range(rows):
#         print(num, end=" ")
#         num += 1
#     print()


# for row in range(1, 6):

#     for col in range(1, row + 1):
#         print(col, end=" ")

#     print()


# students = ["Amit", "Rahul", "Priya"]
# subjects = ["Math", "Science", "English"]

# for student in students:
#    print(f"\nMarks of {student}")
#    for subject in subjects:
#       print(subject)



students = ["Amit", "Rahul", "Priya"]
subjects = [
    { "Math" : 58, "Science": 67, "English" : 84 },
    { "Math" : 88, "Science": 77, "English" : 89 },
    { "Math" : 67, "Science": 75, "English" : 79 },
]      

for student, marks in zip(students, subjects):
   print(f"\nMarks of {student}")

   for subject, mark  in marks.items():
      print(f"{subject} : {mark}")


