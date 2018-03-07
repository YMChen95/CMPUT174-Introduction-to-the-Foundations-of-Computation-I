def copy_list(number_list):
    # Write your function code here
    alist=[]
    for item in number_list:
        alist.append(list(item))
    return alist

def main():
    number_list = [[1, 2, 3], [4, 5, 6], [8, 9], [10]]
    new_list = copy_list(number_list)
    print(number_list)
    print(new_list)
    number_list.pop()
    new_list[0].append([11, 12])
    print(number_list)
    print(new_list)

main()