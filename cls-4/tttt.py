import json
# my_data={
#     "name":"shipon",
#     "age":28,
#     "city":"tangail",
#     "education":["scince", "physics"]
# }

# with open ("person.json", "w") as file:
#     json.dump(my_data,file,indent=4)

with open("person.json", "r") as personOBJfile:
    personobj=json.load(personOBJfile)
    print(personobj['name'])