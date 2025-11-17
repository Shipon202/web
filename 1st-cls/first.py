# num = input("Enter your age: ")
# num = int(num)  # Convert the input to an integer
# print(type(num))  # This will print <class 'int'> to show the type of num
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# num = input("Enter your age")
# num = int(num)
# print(type(num))
# if num % 2 == 0:
#   print( num, "is even")
# else:
#   print(num, "is odd")
# for i in range(10, 0, -1):
#     print(i)
# for i in range(10):
#   print("*" * (i+1))

# def add_3(x):
#   return x + 3
# x = 5
# y = add_3(x)
# print(x, y)

# def greetings():
#   print("hello")

# country = "Bangladesh"
# for c in country:
#   print(c)
#
country = "Bangladesh"
print(country[3])

import math
n = 16
r = math.sqrt(n)
print(r)

def print_multiplication_table(n):
  for i in range(1, 11):
    print(n, "x", i, "=", n * 1)
n = input()
n = int(n)
print_multiplication_table(n)