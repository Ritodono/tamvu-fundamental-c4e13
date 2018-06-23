cm = float(input("height?(cm)"))
h = cm / 100
m = float(input("weight?(kg)"))
BMI = (m) / (h*h)
if BMI < 16:
    print("Severely underweight")
if 16 < BMI < 18.5:
    print("underweight")
if 18.5 < BMI < 25:
    print("normal")
if 25 < BMI < 30:
    print("overweight")
if BMI > 30:
    print("obese")























