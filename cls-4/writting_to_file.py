# with open("demo.text","w") as file:
#     file.write("hello")
#     print("ok.....")

# with open("demo.text", "r") as file:
#     content = file.read()
#     print(content)


# import os
# os.rename("demo.text", "new.text")

# import os
# from os import rename

# os.mkdir("new_dir")
# os.rename("new_dir","shipon")
# os.rmdir("shipon")
# import os



# with open("shipon/new.text", "a") as file:
#     file.write("hello")


import csv
# my_result=[
#     ['Name', 'subject', 'mark'],
#     ['himo', 'math', '80'],
#     ['akkas', 'bangla', '90'],
#     ['jhon', 'math', '80'],
#     ['rock', 'bangla', '90']
# ]
# with open("report.csv",'w') as file:
#     new_writer=csv.writer(file)
#     new_writer.writerows(my_result)
#     print("completed")


# my_result = []
# with open("report.csv", 'r') as file:
#     new_reader = csv.reader(file)
#
#     # for row in new_reader:
#     #     print(row)
#     for row in new_reader:
#         my_result.append(row)
# print(my_result)


import json
my_data={
    "name":"shipon",
    "age":28,
    "city":"tangail",
    "education":["scince", "physics"]
}
# with open('new.json','w')as file:
#     json.dump(my_data,file,indent=4)
#     print("compeleted")

# import json
with open ('new.json','r') as file:
    my_data = json.load(file)
    print(my_data['city'])


### error catch

#
# import json
# from logging import exception
#
# try:
#     with open('new.json', 'r')as file:
#         my_data = json.load(file)
#         print(my_data['name'])
# except Exception as error:
#     print(error)
# finally:
#     print('connection off...')


