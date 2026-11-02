units=int(input("enter the units: "))
fixed_charge=int(input("enter the fixed charge : " ))
if units <= 100:
    bill_charge=units*2
elif units <= 200:
    bill_charge=(100*2)+((units - 100)*3)
else:
    bill_charge=(100*2)+(100*3)+((units-200)*5)
total_bill=fixed_charge+bill_charge
print(f"units consumed:{units}")
print(f"fixed charge:{fixed_charge}")
print(f"bill  amount charged:{bill_charge}")
print(f"total bill chared:{total_bill}")