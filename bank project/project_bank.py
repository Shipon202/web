class bank:
    __balance = 0
    def deposite(self,amount):
        if amount<=0:                   # 0 theke kom hoylay
            print("invaild amount")
        else:
            self.__balance += amount
            print("successfully deposite")


    def withdraw(self, amount):
      if amount<0:
          print("invaild withdraw")
      elif amount>self.__balance:
          print("ato tk nai")

      else:
            self.__balance -= amount
            print("successfully withdraw")
    def check(self):
        print(f"my balance is {self.__balance}")

object=bank()
object.check()
object.deposite(100)
object.check()
object.withdraw(50)
object.check()
object.withdraw(200)
