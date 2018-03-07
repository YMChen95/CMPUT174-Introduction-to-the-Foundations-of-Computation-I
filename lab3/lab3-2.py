temp=float(input("Enter temperature in Celsius:"))
if temp<=36:
    print("Hypothermia")
elif 36<temp<38.5:
    print("Normal")
elif temp>=38.5:
    print("Feverish")