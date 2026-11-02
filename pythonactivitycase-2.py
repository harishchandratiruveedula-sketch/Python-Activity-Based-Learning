balance=5000
withdrawal_amount=int(input("enter the withdrawal amount: "))
if withdrawal_amount > balance:
    print("Trasanction Rejected: Insufficient Funds ")
else:
    balance=balance-withdrawal_amount
    print("Trasanction Successful!")
    print(f"Remaing balance:{balance}")