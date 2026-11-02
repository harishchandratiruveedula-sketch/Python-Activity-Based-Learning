vehicle=input("enter the type of vehicle : ")
hours=int(input("enter the parking time: "))
if vehicle == "car":
    rate=20
else:
    rate=10
total_fee = hours*rate
if total_fee > 50:
    total_fee = 50
print(f"vehicle type:{vehicle}")
print(f"total parking fee:{total_fee}")