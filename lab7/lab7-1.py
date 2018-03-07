def eliminate_duplicates(inputlist):
    # Write the function code here
    dislist=[]
    for item in inputlist:
        if int(item) not in dislist:
            dislist.append(int(item))
    return dislist
        
def main():
    # Write the main function
    inputstring=input("Enter numbers:")
    inputlist=inputstring.split(" ")
    print("The distinct numbers are",eliminate_duplicates(inputlist))
    list1=[]
    for n in inputlist:
        n=int(n)
        list1.append(n)
    print("The original numbers are",list1)
# Call the main function
main()