def show_balnce():
   print(f"your balance is {balance}")
def deposite():
    pass
def withdraw():
    pass
balance = 0
is_runnig = True

while is_runnig:
    print("welcome banking")
    print("1.show_balance")
    print("2.depostie")
    print("3.withdraw")
    print("4.exited")
    choice = input("enter your choice(1-4): ")
    if choice=='1':
        show_balnce()
    elif choice=='2':
        deposite()
    elif choice=='3':
        withdraw()
    elif choice=='4':
        is_runnig =False
    else:
        print("wrong number")
print("have nice day")