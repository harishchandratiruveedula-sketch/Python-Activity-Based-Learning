before_usage=int(input("enter the consumption data before : "))
after_usage=int(input("enter the consumption data after: "))
saved = before_usage -after_usage
saving_percent=(saved/before_usage)+100
print(f"savings:{saving_percent}")