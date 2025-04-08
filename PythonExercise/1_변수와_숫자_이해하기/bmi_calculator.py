kg = float(input("체중(kg): "))
cm = float(input("키(cm): "))
if cm == 0:
    print("zero division")
else:
    print("BMI: ", round((kg / cm**2) * 10000, 1))