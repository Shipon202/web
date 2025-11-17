import datetime
class my_cls:
    def __init__(self,birthday):
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        self.calculator()
    def calculator(self):
        new = datetime.datetime.now()
        age = new - self.birthday
        self.years = age.days // 365
        self.days = age.days % 365

    def about(self):
        print(f"your age is {self.years} and {self.days}")

birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
obj = my_cls(birthday_input)
obj.about()
