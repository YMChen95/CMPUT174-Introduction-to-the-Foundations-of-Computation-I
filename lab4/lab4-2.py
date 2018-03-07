A=input("Do you want to enter numbers Y/N: ")
if A=="Y":
    number1=int(input("Enter number: "))
    B=input("Do you want to continue entering new numbers: Y/N:")
    N=1
    total=number1
    while B=="Y":
        number2=int(input("Enter number: "))
        total=total+number2
        B=input("Do you want to continue entering new numbers: Y/N:")
        N=N+1
    print("The average of",N,"numbers is: ",total/N)
else:
    print("ZeroDivisionError occured. Average cannot be calculated!")