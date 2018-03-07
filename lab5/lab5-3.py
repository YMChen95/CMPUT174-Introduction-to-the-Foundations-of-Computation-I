user_input=input("Type in a line of text:")
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", " "]
list1=[]
for x in user_input:
    if x not in punctuation:
        list1.append(x)
result="".join(list1)
Fresult=result.lower()
FFresult=Fresult[::-1]
print(FFresult)
if Fresult==FFresult:
    print("Palindrome? True")
else:
    print("Palindrome? False")      