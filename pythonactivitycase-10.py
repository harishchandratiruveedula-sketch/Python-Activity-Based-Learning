category=input("enter the type of vehicle: ")
offence=input("enter the offence: ")
if offence == "speeding":
    print("Fine : 1000")
elif offence == "no helmet":
    print("Fine : 500")
elif offence == "signal jump":
    print("Fine : 1500")
else:
    print("Fine : 0")
    print("INVALID OFFENCE")


