principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter your amount : "))
    if principle<0:
        print("principle does not less then zero")
    else:
        break
while True:
    rate = float(input("Enter your rate : "))
    if rate<0:
        print("rate does not less then zero")
    else:
        break
while True:
    time = int(input("Enter your years : "))
    if time<0:
        print("time does not less then zero")
    else:
        break
total = principle * pow((1+rate/100),time)
print(f"Balance after {time} years: ${total:.2f}")