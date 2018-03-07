import os.path

def main():
    Total_animals=0
    Dangerous=0
    Brown_dangerous=0
    Large_safe=0
    Safe_redcolor_or_hardflesh=0
    endofprogram = False
    try:
        infile=open(input("Enter name of input file: "),"r")
        filename=input("Enter name of output file: ")
        while os.path.isfile(filename):
            filename=input("File Exists. Enter name again:  ")
        outfile=open(filename,"w")
    except IOError:
        print("Error opening file - End of program")
        endofprogram = True
    #If there is not exception, start reading the input file
    if endofprogram == False:
        for line in infile:
            line=line.strip()
            if len(line)==0:
                continue
            if line[0]!="#":
                Total_animals=Total_animals+1
                data=line.split()
                if data[3]=="dangerous":
                    Dangerous=Dangerous+1
                if data[0]=="brown" and data[3]=="dangerous":
                    Brown_dangerous=Brown_dangerous+1
                elif data[1]=="large" and data[3]=="safe":
                    Large_safe=Large_safe+1
                elif data[3]=="safe" and data[0]=="red" or data[2]=="hard":
                    Safe_redcolor_or_hardflesh=Safe_redcolor_or_hardflesh+1
            #Process the file and write the result to display and to the output file
        print("total=", Total_animals)
        print("dangerous=", Dangerous)
        print("brown dangerous=", Brown_dangerous)
        print("large safe=", Large_safe)
        print("safe red color or hard flesh=", Safe_redcolor_or_hardflesh)
        outfile.write("total="+str(Total_animals)+ "\n")
        outfile.write("dangerous="+str(Dangerous)+ "\n")
        outfile.write("brown dangerous="+str(Brown_dangerous)+ "\n")
        outfile.write("large safe="+str(Large_safe)+ "\n")
        outfile.write("safe red color or hard flesh="+str(Safe_redcolor_or_hardflesh)+ "\n")
        outfile.close()  
        infile.close()        
main() # Call the main to execute the solution