def sum_digits(number):
    my_list=[]
    for value in range(len(str(number))):
        the_number=number%10
        number=number//10
        my_list.append(the_number)
    return sum(my_list)
def main():
    number=int(input("Enter a number:"))
    print("Sum of digits:",sum_digits(number))   
main()
