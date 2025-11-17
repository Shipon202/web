#***** single-inhertance ********

# class member1:
#     x = 10
#     y =20
#     def add(self):
#         sum = self.x + self.y
#         print(sum)
#
#
# class member2(member1):
#     pass
#
# obj= member2()
# obj.add()
#
# obj1=member1()
# obj1.add()



#**********  multipul inheretainc *****
# class member1:
#     x = 10
#     y =20
#     def add(self):
#         sum = self.x + self.y
#         print(sum)
#
# class member3:
#     a = 90
#     b =20
#     def add2(self):
#         sum2 = self.a - self.b
#         print(sum2)
#
# class member2(member1, member3):
#     pass
#
# object = member2()
# object.add()
# object.add2()


# ***** overriding ****

# class Frist_year:
#     m=90
#
#     def marks(self):
#         math=self.m
#         print(math)
#
# class Second_year:
#     m=80
#     def marks(self):
#         math = self.m
#         print(math)
#
# object = Second_year()
# object.marks()


#**** abstruction *******


# from abc import ABC,abstractmethod
#
# class Frist_year(ABC):
#     m=90
#     n = 80
#     @abstractmethod
#     def marks(self):
#         math=self.m + self.n
#         print(math)
#     # @abstractmethod
#     def marks2(self):
#         math = self.m - self.n
#         print(math)
#
# class Sceond_year(Frist_year):
#     def marks(self):
#         math = self.m + self.n
#         print(math)
#
#
# object= Sceond_year()
# object.marks()
# object.marks2()




#**** over lodaing ****

# class exam:
#     def mark(self,a=0, b=0, c=0, d=0,):
#         sum = a+b+c+d
#         print(sum)
#
#     # varaible lenght arg
#
#     def exam2(self,*marks):
#         print(marks)
#
# object = exam()
# object.mark(10)
# object.mark(10,20)
# object.mark(10,20,30)
# object.mark(10,20,30,4)
#
# object.exam2("a")
# object.exam2("a","b")
# object.exam2("a","b","c")
# object.exam2("a","b","c","d")


#**** static method *******

class mark:
    x =10
    y =20
    @staticmethod
    def add():
        sum = mark.x + mark.y
        print(sum)
mark.add()


