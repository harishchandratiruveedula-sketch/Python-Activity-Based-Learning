units=float(input("enter water consumed in units: "))
fixed_units=int(input("enter the fixed units: "))
penalty=100 if units > 30 else 0
if units < 0:
    print("invalid consumption")
else:
    if units <=10:
        bill=units*5
    elif units <= 20:
        bill=50 +(units - 10)
    else:
        bill=130 +(units - 20)*12
    total=bill+fixed_units+penalty
    print(f"total water bill:{total}")
