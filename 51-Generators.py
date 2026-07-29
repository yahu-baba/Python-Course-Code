
# def fruits():
#    yield "Apple"
#    yield "Banana"
#    yield "Grapes"

# g = fruits() 

# next(g)
# print("Message 1")
# print("Message 2")
# next(g)
# print("Message 3")
# print("Message 4")
# print("Message 5")
# print(next(g))


# def fruits():
#    yield "Apple"
#    yield "Banana"
#    yield "Grapes"

# for i in fruits():   
#    print(i)




def squares(n):

   for i in range(1, n + 1):
      yield i * i

for value in squares(10): 
      print(value)