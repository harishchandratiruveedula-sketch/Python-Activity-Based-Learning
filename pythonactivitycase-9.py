password=input("enter the password: ")
if len(password) < 8:
    print("invaild:must contain at least 8 characters ")
elif password.islower():
    print("invalid:must contain  an uppercase character ")
elif password.isupper():
    print("invalid:must contain an lower case character")
elif password.isalpha():
    print("invalid:must contain an number or symbol")
else:
    print("invalid password")