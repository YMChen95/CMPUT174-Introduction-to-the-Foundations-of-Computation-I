C=float(input("How many centimetres do you want to convert? "))
Y=C//(36*2.54)
F=(C-Y*36*2.54)//(12*2.54)
I=(C-Y*36*2.54-F*12*2.54)/2.54
print("This is ",Y,"yards, ",F,"feet, ",I,"inches.")
