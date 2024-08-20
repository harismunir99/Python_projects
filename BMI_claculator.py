
print("This is  a BMI Calculator")
print("-------------------------\n")

name = input("Enter your Name: ")
weight = float(input("Enter your Weight: "))
height = float(input("Enter your Height: "))

bmi = weight / (height/100) ** 2

if (bmi < 18.5):
    print(f"{name}, You are under weight. Your BMI is {bmi}")
    
if (bmi >= 18.5 and bmi < 24.999):
    print(f"{name}, You are Normal and Healthy. Your BMI is {bmi}")
    
if (bmi >= 25 and bmi < 29.9):
    print(f"{name},You are overweight, Please have a diet. Your BMI is {bmi}")
    
if (bmi >= 30 and bmi < 34.9):
    print(f"{name}, You are obase, Please do exercise. Your BMI is {bmi}")
    
if (bmi >= 35):
    print(f"{name}, You are extremely obase, Please consult a doctor. Your BMI is {bmi}")
