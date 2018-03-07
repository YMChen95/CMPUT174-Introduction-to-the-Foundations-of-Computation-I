def mylen(alist):
    if len(alist)==0:
        return 0
    return 1+mylen(alist[1:])

def main():
    alist=[43,76,97,86]
    blist=[]
    print(mylen(alist))

main()