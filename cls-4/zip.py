import zipfile
#
# with zipfile.ZipFile("new2.zip", "w") as zip:
#     zip.write("project-1.py")

with zipfile.ZipFile('new2.zip', 'r')as zip:
    zip.extractall()
    my_file = zip.namelist()
    print(my_file)