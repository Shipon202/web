# import random
# numbers = []
# for _ in range(10):
#     numbers.append(random.randint(1, 100))
# print(numbers)
# # numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_number = float('-inf')
# for n in numbers:
#     if n > max_number:
#         max_number = n
# print(max_number)


# def my_sum(a, b, c):
#     n = (a + b + c) * 2
#     return n
# x = my_sum(1,2,3)
# print(x)


# def sum(a,b,c):
#     global d
#     d=d*2
#     a*=2
#     b*=2
#     c*=2
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
#     print("d=",d)
#     n=a+b+c
#     return n
# a=10
# b=20
# c=30
# d=40 #this is gobal variable
# x=sum(a,b,c)
# print(x)
# print("a=", a)
# print("b=", b)
# print("c=", c)

# def print_multiplication_table(n):
#   for i in range(1, 11):
#     print(n, "x", i, "=", n * 1)
# n = input("Enter a number : ")
# n = int(n)
# print_multiplication_table(n)

# def my_f(a,b,c=0):
#     n=a+b+c
#     return n*2
# x=my_f(10,20)
# y=my_f(10,20,30)
# print(x)
# print(y)

# def sum (a,b,c):
#     global d
#     d=d*2
#     n = a+b+c
#     return n*2
# def anoter_fnc():
#     print(d)
# d=100
# x=sum(10,20,30)
# print(x)
# print(d)


# def l_fnc(li):
#     return max(li)
# import random
# num = []
# for _ in range(1,10):
#     num.append(random.randint(1,50))
#     print(num)
# x = l_fnc(num)
# print(x)

def my_fnc(li,n):
    li[0] = 100
    n=20
    return max (li)
nums = [10,20,30,40]
n=10
x=my_fnc(nums, n)
print(x)
print("n==", n)