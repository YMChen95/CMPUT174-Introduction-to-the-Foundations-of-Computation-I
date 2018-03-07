user_input=input("Type in a line of text: ")
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", " "]
list1=[]
for x in user_input:
    if x not in punctuation:
        list1.append(x)
print(list1)
results="".join(list1)
print(results)