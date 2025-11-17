email = input("Enter your email name : ")
index = email.index("@")
user_name = email[:index]
domen_name = email[index + 1 :]

print(f"your user name is {user_name} and domen is {domen_name}")