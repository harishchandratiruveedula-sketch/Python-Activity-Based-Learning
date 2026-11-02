student_name=input("enter the student: ")
score=int(input("enter student score: "))
student_attendence=int(input("enter student attendence percentage: "))
min_score=85
min_attendence=75
if score >= min_score and student_attendence >= min_attendence:
    print("status: ELIGIBLE FOR SCHOLARSHIP")
    if score >= 95:
        print("Tier:Full Scholarship (100% tuition coverage)")
    else:
        print("Tier:Partial Scholarship(50% tuition coverage)")
else:
    print("Status:NOT ELIGIBLE")
