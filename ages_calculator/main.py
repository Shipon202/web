import datetime
def calculator(brithday):
    brithday = datetime.datetime.strptime(brithday, "%Y-%m-%d")
    new = datetime.datetime.now()
    age = new - brithday
    years = age.days // 365
    days = age.days % 365
    return years, days

brithday_int = input("enter your ages (YYYY-MM-DD): ")
object = calculator(brithday_int)
print(f"Age: {object[0]} years and {object[1]} days")




