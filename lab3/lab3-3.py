lab=float(input("what is your lab mark?(out of 100):"))
assign=float(input("what is your assign mark?(out of 100):"))
mid=float(input("what is your midterm mark?(out of 100):"))
exam=float(input("what is your exam mark?(out of 100):"))
lab1=lab*0.15
assign1=assign*0.25
mid1=mid*0.25
exam1=exam*0.35
total=round(lab1+assign1+mid1+exam1,2)
if total>=90:
    print(total,"% is a A+")
elif 85<=total<90:
    print(total,"% is a A")
elif 80<=total<85:
    print(total,"% is a A-")
elif 76<=total<80:
    print(total,"% is a B+")
elif 73<=total<76:
    print(total,"% is a B")
elif 70<=total<73:
    print(total,"% is a B-")
elif 66<=total<70:
    print(total,"% is a C+")
elif 63<=total<66:
    print(total,"% is a C")
elif 60<=total<63:
    print(total,"% is a C-")
elif 55<=total<60:
    print(total,"% is a D+")
elif 50<=total<55:
    print(total,"% is a D")
elif 0<=total<50:
    print(total,"% is a F")