def main():
    cities={}
    stop=False
    while not stop:
        userinput=input("Enter city followed by temperature:")
        if userinput!="stop":
            space=userinput.index(" ")
            city=userinput[0:space]
            temp=int(userinput[space+1:])
            cities[city]=int(temp)
            lowest=temp
            coldestcity=""
            for key in cities:
                if cities[key]<=lowest:
                    lowest=cities[key]
                    coldestcity=key
        else:
            print(cities)
            stop=True
            print("The coldest city is", coldestcity, lowest)
            
main()