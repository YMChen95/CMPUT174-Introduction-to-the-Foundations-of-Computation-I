user_input=input("Enter word:")
list1=[]
for x in user_input:
    list1.append(x)
    list2=list1[::-1]
if list1==list2:
    print("Palindrome? True")
else:
    print("Palindrome? False")