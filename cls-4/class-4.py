# current_tem = 31
# reference_tem =28
# result = current_tem == reference_tem
# result = current_tem % 2 == 0
# print(result)
# if result:
#     print(current_tem, "is an even number")
# else:
#     print(current_tem, "is an even number")

# today = input("Enter the day:")
# today = today.title()
# public_holiday = input("is today a public holiday? (yes/no)")
# public_holiday = public_holiday.lower()
# sick_today = input("are you sick today?(yes/no)")
# sick_today = sick_today.lower()
# print(today == "sunday" or today == "saturday")

# if today == "sunday" or today == "saturday" or public_holiday == "yes" or sick_today == "yes":
#     print("off day")
# elif today == "saturday":
#     print("off day")
# elif public_holiday == "yes":
#     print("off day")
# elif sick_today == "yes":
#     print("off day")
# else:
#     print("you are out off time" + " "+"Go to office")

# m_buget = 2000
# m_brand = "Toyota"
# m_color ="red"
# maximum_M = 30000

# car1_price =19000
# car1_brand = "bmw"
# car1_color = "white"
# mileage = 20000

# def meets_req(price, brand, color, mileage):
#     m_buget = 2000
#     m_brand = "Toyota"
#     m_colors = ["red", "white", "black", "bronze"]
#     maximum_M = 30000
#
#     if (price <= m_buget and brand == m_brand and color in m_colors and mileage <= maximum_M) or (price<= m_buget//2 and 30000 < mileage<=40000):
#          return True
#
#     # print("yes , u can buy a car")
#
#
#
#     else:
#     # print("u can not buy a car")
#         return False
# p = input("what is your price")
# p = int(p)
# brand = input("which brand")
# color =input("color")
# mileage = input("how many km")
# mileage = int(mileage)
#
# if meets_req(p, brand, color, mileage):
#     print("yes, consider this car")
# else:
#     print("no u can not buy a car")

# for loop class
# result = 0
# for i in range(1, 101, 4):
#     result = result + i
#     print("Result:", result, "i =", i)
# print(result)


#while loop
# result = 0
# i= 1
# while i <= 100:
#     result = result + i
#     i+=4
#     print("Result:", result, "i =", i)
# print(result)

# def add_1_to_n(n):
#     result = 0
#     for i in range(1, n+1):
#         result = result + i
#     return result
# n = input("enter your number: ")
# n = int(n)
# while n != 0:
#     if n == 0:
#      print("enter a vaild number")
#     r = 0
#     for i in range(1, n+1):
#         r = r+1
#     print(r)
#     n = input("enter your number: ")
#     n = int(n)

# for num1 in range(1, 6):
#     for num2 in range(1, 6):
#         print(num1, num2, num1 + num2)
class mark:
    x =10
    y =20
    @staticmethod
    def add():
        sum = mark.x + mark.y
        print(sum)
mark.add()

