
# numbers = [1, 2, 3, 4, 5]

# def square(n):
#    return n * n

# result = map(square, numbers) 

# print(list(result))



# names = ["amit", "rahul", "priya"]

# # result = map(str.upper, names)
# result = map(len, names)

# print(list(result))



# prices = [100, 250, 500]

# # def add_gst(price):
# #    return price + (price * 0.18)

# # result = list(map(add_gst, prices))

# result = list(map(lambda price: price + (price * 0.18), prices))

# print(result)



price = [100, 200, 300]

gst = [18, 12, 5]

result = map(lambda p, g: p + (p * g / 100), price, gst)

print(list(result))
