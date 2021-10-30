print("Body Mass Index calculator")
print("-"*75)
#enter
height= float(input("Enter your height(m):"))
weight= float(input("Enter your weight (kg):"))
pol= str(input("Enter your gender (M/F): "))
#account
bmi= weight/(height**2)

print("-"*75)
#preview
print("Your BMI is: ", float(bmi))
print("-"*75)

#logic
if pol=="M" or pol=="m":
    if bmi < 20.7:
        print("BMI too low for male!")
    elif bmi < 26.4:
        print("BMI ideal for male!")
    elif bmi < 27.8:
        print("BMI slightly above normal for male!")
    elif bmi < 31.1:
        print("BMI high for male!")
    elif bmi < 45.4:
        print("BMI too high for male!")
    else:
        print("BMI extremely high for male!")
elif pol=="F" or pol=="f":
    if bmi < 19.1:
        print("BMI too low for female!")
    elif bmi < 25.8:
        print("BMI idealfor female!")
    elif bmi < 27.3:
        print("BMI slightly above normal for female!")
    elif bmi < 32.2:
        print("BMI high for female!")
    elif bmi < 44.8:
        print("BMI too high for female!")
    else:
        print("BMI extremely high for female!")
else:
    print("You must define the gender exactly to get the calculation of BMI.")