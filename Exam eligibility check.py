medical_cause=input("did you have a medical cause? Yes or No?: ")
attend=int(input("enter the attendance of the student: "))

if medical_cause =="Yes":
    print("You are allowed")

else:
    if attend>=75:
        print("Allowed")

    else:
        print("Not allowed")
