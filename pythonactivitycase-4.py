emp_name=input("enter the  employee name : ")
salary=int(input("enter the employee salary: "))
allowances=int(input("enter the employee allowances: "))
total_salary=salary+allowances
if total_salary > 60000:
    tax = total_salary*0.20
else:
    tax = total_salary*0.10
net_salary = total_salary-tax
print(f" employee total salary:{total_salary}")
print(f"employee payed the tax:{tax}")
print(f"employee net salary:{net_salary}")