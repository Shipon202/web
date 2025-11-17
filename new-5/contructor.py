# import datetime
# print(datetime.datetime.now())

# class My_class:
#     name= 'shipon'
#     age = '28'
#     def about(self,city):
#         print(f"my name is {self.name} and is {self.age} and city is {city}")
# obj=My_class()
# # print(obj.name)
# obj.about("dhaka")


#******* Constructor ******

class My_class2():
    name = "shipon"
    age = 28
    def about(self):
        print(f"my name is {self.name} and ages is {self.age}")


    def __init__(self, num1, num2, agevalue, datevalue):
        sum = num1 + num2
        print(f"the sum is {sum}")
        self.dateofbith=datevalue

        self.age=agevalue
obj= My_class2(10, 20, 30, "31-05-1997")
obj.about()
print(obj.dateofbith)
