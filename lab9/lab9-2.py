def main():
    my_dict={}
    numbers=input("Enter numbers separated by spaces:")
    numbers=numbers.split()
    for number in numbers:
        if number in my_dict:
            my_dict[number]=my_dict[number]+1
        else:
            my_dict[number]=1
    print(my_dict)
    for key in my_dict:
        if my_dict[key]>1:
            print(key,"occurs",my_dict[key],"times")
        else:
            print(key,"occurs one time")
    

main()