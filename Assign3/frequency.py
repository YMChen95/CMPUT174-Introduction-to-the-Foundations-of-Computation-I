
def printsection1(animals, station1, station2):
        print("Number of times each animal visited each station : ")
        print("Animal Id"+11*" "+"Station 1"+11*" "+"Station 2"+11*" ")
        #Use the getting method to count how many in each station
        #If there is no objects, return 0
        for i in animals:
                s1=str(station1.get(i,0))
                s2=str(station2.get(i,0))
                print(i+(20-len(i))*" "+s1+(20-len(s1))*" "+s2+(20-len(s2))*" ")
                #In right order
                animals.sort()
        return
    
    
    
def printsection2(animals, station1, station2):
        print('Animals that visited both stations at least 4 times')
        #Use the get method to count and compare with 4
        for i in animals:
                if station1.get(i,0)>=4 and station2.get(i,0)>=4:
                        print(i)
        return




def printsection3(animals,station1,station2):
        print('Total Number of visits for each animal')
        #Get how many animals in each station
        #Convert int to str in order to use "+" to combine
        for i in animals:
                print(i+20*" "+str(station1.get(i,0)+station2.get(i,0)))   
                animals.sort()
        return i




def printsection4(items):
        print('the month that has the highest number of visits to the stations ')
        #Create frequency as a dictionary and month as a list
        frequency={}
        monthlist=[]
        for i in items:
                month=i[1][0:2]
                #Set the frequency
                if month not in frequency:
                        frequency[month]=1
                else:
                        frequency[month]=frequency[month]+1
                #Set the month
                if month not in monthlist:
                        monthlist.append(month)
                #Output the month which is the highest vistors
        for index in range(len(monthlist)-1,-1,-1):
                if frequency[monthlist[index]]==max(frequency.values()):
                        print(monthlist[index])
                        break
        return

def main():
        #Create variables
        station1={}
        station2={}
        record=()
        items=[]
        animals=[]
    
        #Error Handing
        isProgram=True
        try:
                infile=open(input("Enter name of input file >"))
        except IOError:
                print("File does not exist")
                isProgram=False
                   
        #Running if isProgram is True
        if isProgram==True:
                for line in infile:
                        #"Get rid of useless stuff, like ":" and "#"
                        if line[0]!="#" and line[0]!="\n":
                                line=line.strip("\n")
                                AnimalId,Timestamp,StationId=line.split(":")
                                record=(AnimalId,Timestamp,StationId)
                                items.append(record)
                                if AnimalId not in animals:
                                        animals.append(AnimalId)
                                #Set the station
                                if StationId=="s1":
                                        station=station1
                                else:
                                        station=station2
                                if AnimalId not in station:
                                        station[AnimalId]=1
                                else:
                                        station[AnimalId]=station[AnimalId]+1
    
                #Output
                printsection1(animals, station1, station2)
                print(60*'=')
                printsection2(animals, station1, station2)
                print(60*'=')
                printsection3(animals,station1,station2)
                print(60*'=')
                printsection4(items)
                infile.close()    
main()