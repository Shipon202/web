weight = float(input("enter your weight :"))
units = input("Kilogram or pounds ? (k or L) : ")
if units == "k":
    weight = weight * 2.205
    units="Lbs."
    print(f"your weight is : {round(weight,1)}  {units}")


elif units == "L":
    weight = weight / 2.205
    units="Kg."
    print(f"your weight is : {round(weight,1)} {units}")

else:
    print(f"{units} was not vaild")