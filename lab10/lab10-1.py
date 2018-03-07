def reverseDisplay(number):
    if number!=0:
        number1=number%10
        number=number//10
        print(number1,end='')
        return reverseDisplay(number)
    
def main():
    number = int(input("Enter a number: "))
    reverseDisplay(number)
    print(reverseDisplay(number))

main()